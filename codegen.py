#!/usr/bin/env python3

import sys

def print_usage():
    print('usage: codegen.py <language>')
    print('LANGUAGE:')
    print('py / python     Python3')
    print('c# / csharp     C#')
    print('c++ / cpp       c++')

def generate_python():
    with(open('main.py','w') as f):
        f.write('#!/usr/bin/env python3\n')
        f.write('\n')
        f.write('if __name__ == "__main__":\n')
        f.write('  print(\'Hello, friend!\')')

def generate_csharp():
    with(open('main.cs','w') as f):
        f.write('using System;\n')
        f.write('using System.Collections.Generic;')
        f.write('\n')
        f.write('namespace Application\n')
        f.write('{\n')
        f.write('  public static class Program\n')
        f.write('  {\n')
        f.write('    public static int Main(string[] args)')
        f.write('    {\n')
        f.write('      Console.WriteLine("Hello, friend!");\n')
        f.write('      return 0;')
        f.write('    }\n')
        f.write('  }\n')
        f.write('}\n')

def generate_cpp():
    with(open('main.cpp','w') as f):
        f.write('#include <iostream>\n')
        f.write('\n')
        f.write('int main(int argc, char** argv)\n')
        f.write('{\n')
        f.write('  std::cout << "Hello, friend!" << std::endl;')
        f.write('  return 0;')
        f.write('}\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('EE: invalid command line\n')
        print_usage()
        sys.exit()

    supported_languages = {
        'py' : generate_python,
        'python' : generate_python,
        'c#' : generate_csharp,
        'csharp' : generate_csharp,
        'c++' : generate_cpp,
        'cpp' : generate_cpp
    }

    try:
        supported_languages[sys.argv[1]]()
    except:
        print(f'EE: Language \'{sys.argv[1]}\' is not supoprted\n')
        print_usage()

