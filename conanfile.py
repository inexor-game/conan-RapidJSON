from os.path import join as path_join
from conans import ConanFile, CMake

class RapidJSONConan(ConanFile):
    name = "RapidJSON"
    version = '1.0.2'
    url = 'https://github.com/SamuelMarks/conan-rapidjson'
    license = 'SQLite'
    exports = 'RapidJSONConfig.cmake'

    def source(self):
        self.run("git clone https://github.com/miloyip/rapidjson")
        self.run("cd rapidjson && git checkout v%s" % self.version)

    def package(self):
        self.copy('RapidJSONConfig.cmake', '.', '.')
        self.copy('*', dst='include', src='rapidjson/include')

    def build(self):
        pass
