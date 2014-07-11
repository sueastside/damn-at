"""
Does some stuff
"""
import os
import unittest

#import logging
#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from damn_at.pluginmanager import DAMNPluginManagerSingleton
from damn_at.analyzer import Analyzer

def pretty_print(file_descr):
    """Pretty print the file_descr"""
    print(file_descr.file.filename)
    if file_descr.assets:
        for asset in file_descr.assets:
            print('', asset.asset.subname, asset.asset.mimetype, asset.asset.file.filename)
            if asset.dependencies:
                for dep in asset.dependencies:
                    print('  ', dep.subname, dep.mimetype, dep.file.filename)


class TestCase(unittest.TestCase):
    """Test case"""
    def rtest_say(self):
        """Test say"""
        # Build the manager
        simple_plugin_mgr = DAMNPluginManagerSingleton.get()
        print(simple_plugin_mgr.getAllPlugins())

        # Activate all loaded plugins
        for plugin_info in simple_plugin_mgr.getAllPlugins():
            print('Activating', plugin_info.name)
        for plugin_info in simple_plugin_mgr.getPluginsOfCategory('Failed'):
            print('E: ', plugin_info.name, plugin_info.error)
        assert True
        
    def test_analyze(self):
        """Test say"""
        totest = []
        for root, dirs, files in os.walk('../damn-test-files'):
            if len(files) != 0:
                totest.append(root+'/'+files[0])
        for totestfile in totest:         
            if '.git' not in totestfile:
                descr = Analyzer().analyze_file(totestfile)
                pretty_print(descr)
        assert True
        

def test_suite():
    """Return a list of tests"""
    return unittest.TestLoader().loadTestsFromTestCase(TestCase)

if __name__ == '__main__':
    #unittest.main()
    unittest.TextTestRunner().run(test_suite())
