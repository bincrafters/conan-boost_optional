#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostOptionalConan(base.BoostBaseConan):
    name = "boost_optional"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_optional"
    lib_short_names = ["optional"]
    header_only_libs = ["optional"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_move",
        "boost_predef",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]
