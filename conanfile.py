from os.path import join as path_join
from conans import ConanFile, CMake

class RapidJSONConan(ConanFile):
    name = 'RapidJSON'
    version = '1.0.2'
    url = 'https://github.com/SamuelMarks/conan-rapidjson'
    license = 'SQLite'
    exports = 'FindRapidjson.cmake' #, '*rapidjson.h'
    settings = None
    options = None # {'header_only': [True]}

    def package(self):
        self.copy('FindRapidjson.cmake', '.', '.')
        #self.copy(src='*rapidjson.h', dst='.', keep_path=False)
        self.copy('*', dst='include', src='rapidjson/include/rapidjson')

    def build(self): pass

    def package_info(self):
        self.cpp_info.libs = ['rapidjson']
