# miscellaneous

from cat.namespace import *
ns = NameSpace()

@define(ns, 'del_word')
def del_word( cat ) :
    '''
    del_word : (string:name -> --)
    
    desc:
        deletes the definition of the word from the current user namespace
        Note: the name may be of the form: word1,word2,...  (e.g. 'test,junk,smmpt)
              of a list  (e.g. ['test 'junk 'smmpt] list
        Words may have the form: <namespace>:<word>
        name: the name of the word to be deleted
    tags:
        words,delete
    '''
    words = cat.stack.pop_list()
    
    for word in words :
        if word.count( ":" ) == 1 :
            ns, wrd = word.split( ":" )
            cat.ns.delWord( wrd, ns )
        
        else :
            cat.ns.delWord( word )

@define(ns, 'del_var')
def del_var( cat ) :
    '''
    del_var : (string:name -> --)
    
    desc:
        removes user variable from symbol table
        Note: name can be a string of the form: name1,name2,...   (e.g. 'var1,test)
              or a list  (e.g. ['var1 'test]). The name of the var may also take the
              form <namespace>:<var name>
        name: the name of the variable to be deleted
    tags:
        user_variables,delete
    '''
    names = cat.stack.pop_list()
    
    for name in names :
        if name.count(":") == 1 :
            ns, name = name.split(":")
            cat.ns.delVar( name, ns )
        
        else :
            cat.ns.delVar( name )

@define(ns, 'del_instance')
def del_instance( cat ) :
    '''
    del_instance : (string:name -> --)
    
    desc:
        Delete the named instance
        name: the instance's name, or a string of the form: <name>,<name>,...
              where <name> ::= {<namespace>:}?<inst name>
    tags:
        instance,delete
    '''
    names = cat.stack.pop_list()
    
    for name in names :
        if name.count(':') == 1 :
            ns, name = name.split( ":" )
            cat.ns.delInst( name, ns )
        
        else :
            cat.ns.delInst( name )

@define(ns, 'get_all_words')
def getAllWords( cat ) :
    '''
    get_all_words : (-- -> list:words)
    
    desc:
        Gets a list of all words (their names as strings) and pushes it onto the stack
        words: the list of word names
    tags:
        words,list
    '''
    cat.stack.push( cat.ns.allWordNames() )
    
def _returnNS() :
    return ns
