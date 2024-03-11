import argparse

#==============================================
#TODO - add support for other languages to be supported in the future

LANG_DICT = {'python': 'py'}

#==============================================

def generate_basic_quine(n_lines,
                         lang = 'python',
                         template = 'exec'): 
    '''
    this function generates an N-line quine from a template source file 
    '''
    
    file_ext = LANG_DICT[lang]
    f = open('{}_quine_lines_{}.{}'.format(lang,
                                           n_lines,
                                           file_ext),'w')

    quine_template = open('./quine_templates/{}_{}_quine.{}'.format(lang,template,file_ext),'r').read().strip()

    for i in range(n_lines):
        f.write(quine_template)
        f.write('\n')
    
    f.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--lines',
                        type = int,
                        default = 5,
                        help = 'number of lines for the quine')
    parser.add_argument('--lang',
                        type = str,
                        default = 'python',
                        help = 'language to use')
    parser.add_argument('--template',
                        type = str,
                        default = 'exec',
                        help = 'quine template type')

    args = parser.parse_args()
    generate_basic_quine(n_lines = args.lines,
                         lang = args.lang,
                         template = args.template)


    
