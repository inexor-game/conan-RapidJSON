# Edited from https://github.com/memsharded/conan-spdlog/blob/master/test_package/conanfile.py
from conans import ConanFile, CMake
import os


class RapidJSONTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = "RapidJSON/1.1.0@inexorgame/stable"
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        self.run('cmake "%s" %s' % (self.source_folder, cmake.command_line))
        self.run('cmake --build . %s' % cmake.build_config)

    def imports(self):
        self.copy('*.dll', 'bin', 'bin')
        self.copy('*.dylib', 'bin', 'bin')

    def test(self):
        os.chdir('bin')
        self.run('.%sfilterkey' % os.sep)
