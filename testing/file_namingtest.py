import sys
sys.path.insert(0, "../src")
import unittest
import dup_time, file_naming, log

log.setverbosity(5)

class FileNamingTest(unittest.TestCase):
	"""Test file naming"""
	def test_basic(self):
		"""Check get/parse cycle"""
		dup_time.setprevtime(10)
		dup_time.setcurtime(20)

		filename = file_naming.get("inc", volume_number = 23)
		log.Log("Inc filename: " + filename, 5)
		pr = file_naming.parse(filename)
		assert pr and pr.type == "inc", pr
		assert pr.start_time == 10
		assert pr.end_time == 20
		assert pr.volume_number == 23

		filename = file_naming.get("full-sig")
		log.Log("Full sig filename: " + filename, 5)
		pr = file_naming.parse(filename)
		assert pr.type == "full-sig"
		assert pr.time == 20

		pr = file_naming.parse(file_naming.get("new-sig"))
		assert pr.type == "new-sig"
		assert pr.start_time == 10
		assert pr.end_time == 20

	def test_suffix(self):
		"""Test suffix (encrypt/compressed) encoding and generation"""
		filename = file_naming.get("inc", manifest = 1, gzipped = 1)
		pr = file_naming.parse(filename)
		assert pr and pr.compressed == 1
		assert pr.manifest

		filename2 = file_naming.get("full", volume_number = 23, encrypted = 1)
		pr = file_naming.parse(filename2)
		assert pr and pr.encrypted == 1
		assert pr.volume_number == 23

	def test_more(self):
		"""More file_parsing tests"""
		pr = file_naming.parse("duplicity-new-signatures.2002-08-18T00:04:30-07:00.to.2002-08-20T00:00:00-07:00.sigtar.gpg")
		assert pr, pr
		assert pr.type == "new-sig"
		assert pr.end_time == 1029826800L
		

if __name__ == "__main__": unittest.main()