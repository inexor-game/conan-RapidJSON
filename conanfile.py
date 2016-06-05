from os.path import join as path_join
from conans import ConanFile, CMake

class RapidJSONConan(ConanFile):
    name = 'RapidJSON'
    version = '1.0.2'
    url = 'https://github.com/SamuelMarks/conan-rapidjson'
    license = 'SQLite'
    #settings = 'os', 'compiler', 'build_type', 'arch'
    exports = '*rapidjson.h'

    def package(self):
        self.copy(path_join('rapidjson', 'include', 'rapidjson', 'rapidjson', 'rapidjson.h'), dst='include')
