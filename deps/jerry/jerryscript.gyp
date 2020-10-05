{
  'targets': [
    {
      'target_name': 'jerrylib',
      'type': 'static_library',
      'actions': [
        {
          'action_name': 'jerrylib',
          'inputs': [
            'jerryscript/tools/build.py',
          ],
          'outputs': [
            'jerryscript/build/lib/libjerry-core.a',
            'jerryscript/build/lib/libjerry-ext.a',
            'jerryscript/build/lib/libjerry-port-default.a',
          ],
          'action': [
            'python',
            'jerryscript/tools/build.py',
            '--cmake-param=-DCMAKE_C_COMPILER_WORKS=TRUE',
            '--compile-flag=-g',
            '--debug',
            '--clean',
            '--error-messages=on',
            '--line-info=on',
            '--cpointer-32bit=on',
            '--mem-heap=16384',
            '--jerry-debugger=on',
            '--strip=OFF'
          ],
        },
      ],
    },
    {
      'target_name': 'jerryapi',
      'type': 'static_library',
      'dependencies': [
        'jerryscript.gyp:jerrylib',
         '<(icu_gyp_path):icui18n',
         '<(icu_gyp_path):icuuc',
      ],
      'include_dirs': [
         'include',
         'jerryscript/jerry-core/include',
         'jerryscript/jerry-port/default/include',
         'jerryscript/jerry-ext/include',
         'v8jerry',
      ],
      'link_settings': {
        'libraries': [
                       '-L<(PRODUCT_DIR)/../../deps/jerry/jerryscript/build/lib -ljerry-core -ljerry-ext -ljerry-port-default'
                       ],
      },
      'sources': [
        'api.cc',
        'api_ext.cc',
        'inspector.cc',
        'platform.cc',

        'v8jerry/v8jerry_allocator.cpp',
        'v8jerry/v8jerry_allocator.hpp',
        'v8jerry/v8jerry_backing_store.cpp',
        'v8jerry/v8jerry_backing_store.hpp',
        'v8jerry/v8jerry_allocator.hpp',
        'v8jerry/v8jerry_callback.cpp',
        'v8jerry/v8jerry_callback.hpp',
        'v8jerry/v8jerry_flags.cpp',
        'v8jerry/v8jerry_flags.hpp',
        'v8jerry/v8jerry_handlescope.cpp',
        'v8jerry/v8jerry_handlescope.hpp',
        'v8jerry/v8jerry_isolate.cpp',
        'v8jerry/v8jerry_isolate.hpp',
        'v8jerry/v8jerry_templates.cpp',
        'v8jerry/v8jerry_templates.hpp',
        'v8jerry/v8jerry_utils.cpp',
        'v8jerry/v8jerry_utils.hpp',
        'v8jerry/v8jerry_value.cpp',
        'v8jerry/v8jerry_value.hpp'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'export_dependent_settings': [
        '<(icu_gyp_path):icui18n',
        '<(icu_gyp_path):icuuc',
      ],
    },
  ],
}
