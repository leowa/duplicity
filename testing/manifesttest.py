import sys, unittest, types
sys.path.insert(0, "../src")
import manifest, globals, path

class VolumeInfoTest(unittest.TestCase):
	"""Test VolumeInfo"""
	def test_basic(self):
		"""Basic VolumeInfoTest"""
		vi = manifest.VolumeInfo()
		vi.set_info(3, ("hello", "there"), ())
		vi.set_hash("MD5", "aoseutaohe")
		s = vi.to_string()
		assert type(s) is types.StringType
		#print "---------\n%s\n---------" % s
		vi2 = manifest.VolumeInfo()
		vi2.from_string(s)
		assert vi == vi2

	def test_special(self):
		"""Test VolumeInfo with special characters"""
		vi = manifest.VolumeInfo()
		vi.set_info(3234, ("\n eu \x233", "heuo", '\xd8\xab\xb1Wb\xae\xc5]\x8a\xbb\x15v*\xf4\x0f!\xf9>\xe2Y\x86\xbb\xab\xdbp\xb0\x84\x13k\x1d\xc2\xf1\xf5e\xa5U\x82\x9aUV\xa0\xf4\xdf4\xba\xfdX\x03\x82\x07s\xce\x9e\x8b\xb34\x04\x9f\x17 \xf4\x8f\xa6\xfa\x97\xab\xd8\xac\xda\x85\xdcKvC\xfa#\x94\x92\x9e\xc9\xb7\xc3_\x0f\x84g\x9aB\x11<=^\xdbM\x13\x96c\x8b\xa7|*"\\\'^$@#!(){}?+ ~` '), ("\n",))
		s = vi.to_string()
		assert type(s) is types.StringType
		#print "---------\n%s\n---------" % s
		vi2 = manifest.VolumeInfo()
		vi2.from_string(s)
		assert vi == vi2

	def test_contains(self):
		"""Test to see if contains() works"""
		vi = manifest.VolumeInfo()
		vi.set_info(1, ("1", "2"), ("1", "3"))
		assert vi.contains(("1",), recursive = 1)
		assert not vi.contains(("1",), recursive = 0)

		vi2 = manifest.VolumeInfo()
		vi2.set_info(1, ("A",), ("Z",))
		assert vi2.contains(("M",), recursive = 1)
		assert vi2.contains(("M",), recursive = 0)

		vi3 = manifest.VolumeInfo()
		vi3.set_info(1, ("A",), ("Z",))
		assert not vi3.contains(("3",), recursive = 1)
		assert not vi3.contains(("3",), recursive = 0)
		

class ManifestTest(unittest.TestCase):
	"""Test Manifest class"""
	def test_basic(self):
		vi1 = manifest.VolumeInfo()
		vi1.set_info(3, ("hello",), ())
		vi2 = manifest.VolumeInfo()
		vi2.set_info(4, ("goodbye", "there"), ("aoeusht",))
		vi3 = manifest.VolumeInfo()
		vi3.set_info(34, (), ())
		m = manifest.Manifest()
		for vi in [vi1, vi2, vi3]: m.add_volume_info(vi)

		globals.local_path = path.Path("Foobar")
		m.set_dirinfo()

		s = m.to_string()
		#print "---------\n%s\n---------" % s
		assert s.lower().startswith("hostname")
		assert s.endswith("\n")

		m2 = manifest.Manifest().from_string(s)
		assert m == m2


if __name__ == "__main__": unittest.main()