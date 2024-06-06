from conans import ConanFile, CMake

class ExampleConan(ConanFile):
        build_requires = "libxml2/2.9.8@bincrafters/stable"
        requires = "opencv/2.2@drl/stable"

        def requirements(self):
                self.build_requires("apache-apr/0.9.1@jgsogo/stable")
                self.requires("zlib/1.2.0@conan/stable")