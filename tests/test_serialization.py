"""Test Thrift serialization"""
import unittest

from thrift.protocol import TJSONProtocol, TBinaryProtocol

from damn_at.serialization import SerializeThriftMsg, DeserializeThriftMsg

from damn_at import FileId, AssetId, AssetDescription

class SerializationTest(unittest.TestCase):
    """SerializationTest"""   
    filename = "testfile.blend"
    subname = "myobject"
    mimetype = "x-blender/object"
    protocol = TBinaryProtocol.TBinaryProtocol
        
    def test_FileId(self): # pylint: disable=C0103
        """test_serialization"""
        msg = FileId(filename = SerializationTest.filename)

        data = SerializeThriftMsg(msg, self.protocol)
        
        msg = DeserializeThriftMsg(FileId(), data, self.protocol)

        self.assertEqual(SerializationTest.filename, msg.filename)
        
    def test_AssetId(self): # pylint: disable=C0103
        """test_serialization"""
        fileid = FileId(filename = SerializationTest.filename)
        assetid = AssetId(subname = SerializationTest.subname, mimetype = SerializationTest.mimetype, file = fileid)
        
        data = SerializeThriftMsg(assetid, self.protocol)

        msg = DeserializeThriftMsg(AssetId(), data, self.protocol)

        self.assertEqual(SerializationTest.filename, msg.file.filename)
        self.assertEqual(SerializationTest.subname, msg.subname)
        self.assertEqual(SerializationTest.mimetype, msg.mimetype)
    
    def test_AssetDescription(self): # pylint: disable=C0103
        """test_AssetDescription"""
        fileid = FileId(filename = SerializationTest.filename)
        assetid = AssetId(subname = SerializationTest.subname, mimetype = SerializationTest.mimetype, file = fileid)
        asset_descr = AssetDescription(asset = assetid)
        
        dep = AssetId(subname = SerializationTest.subname, mimetype = SerializationTest.mimetype, file = fileid)
        asset_descr.dependencies = [dep]
        
        data = SerializeThriftMsg(asset_descr, self.protocol)

        msg = DeserializeThriftMsg(AssetDescription(), data, self.protocol)
        
        self.assertEqual(SerializationTest.filename, msg.asset.file.filename)
        self.assertEqual(SerializationTest.subname, msg.asset.subname)
        self.assertEqual(SerializationTest.mimetype, msg.asset.mimetype)
        
        self.assertEqual(dep, msg.dependencies[0])


def test_suite():
    """Generate test suits for json and binary protocols"""
    suite = unittest.TestSuite()
    for protocol in [TJSONProtocol.TJSONProtocol, TBinaryProtocol.TBinaryProtocol]:
        test_class = type(protocol.__name__, (SerializationTest,), dict(protocol=protocol))
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTest(tests)

    return suite

if __name__ == '__main__':
    #unittest.main()
    unittest.TextTestRunner().run(test_suite())
