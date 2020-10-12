import sublime, sublime_plugin
import re
import os


def get_name_from_module( view ):
    matches = view.find_all( "^module .*$" )

    if len( matches ) > 0:
        s = view.substr( matches[0] )

        # get "ui.sys.windows.eventloop" from "module ui.sys.windows.eventloop;"
        a = len( "module " )
        b = s.find( ";" )

        if b == -1:
            b = len( s )

        full_name = s[ a:b ]

        if full_name:
            # get "eventloop" from "ui.sys.windows.eventloop"
            splits = full_name.split( "." )
            splits = list( filter( None, splits ) )

            if splits:
                last_name = splits.pop()

                # get "eventloop.d" from "eventloop"
                last_name += ".d"

                return last_name

    return None


def get_name_from_class( view ):
    # "class ..."
    extractions = []
    regions = view.find_all( r"^class[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_interface( view ):
    # "class ..."
    extractions = []
    regions = view.find_all( r"^interface[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_struct( view ):
    # "struct ..."
    extractions = []
    regions = view.find_all( r"^struct[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_function( view ):
    # "void ...()"
    extractions = []
    regions = view.find_all( r"^[\w]+[\s]+(\w+)[\s]*\(", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_enum( view ):
    # "class ..."
    extractions = []
    regions = view.find_all( r"^enum[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_template( view ):
    # "template ..."
    extractions = []
    regions = view.find_all( r"^template[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name

    # "mixin template ..."
    extractions = []
    regions = view.find_all( r"^mixin[\s]+template[\s]+(\w+)", 0, r"\1", extractions )

    if extractions:
        name = extractions[ 0 ]
        name = name.lower() + ".d"
        return name


def get_name_from_first_line( view ):
    line = view.substr( view.line( 0 ) )
    
    matches = re.search( r"\w+", line )

    if matches:
        name = matches.group()
        return name


class DlangAutoFileName( sublime_plugin.EventListener ):

    def on_modified( self, view ):
        if view.file_name() is None:
            # module path.folder.name
            name = get_name_from_module( view )

            if name:
                view.set_name( name )
                return

            # class Name
            name = get_name_from_class( view )

            if name:
                view.set_name( name )
                return

            # interface Name
            name = get_name_from_interface( view )

            if name:
                view.set_name( name )
                return

            # struct Name
            name = get_name_from_struct( view )

            if name:
                view.set_name( name )
                return

            # struct Name
            name = get_name_from_enum( view )

            if name:
                view.set_name( name )
                return

            # template Name
            name = get_name_from_template( view )

            if name:
                view.set_name( name )
                return

            # function Name
            name = get_name_from_function( view )

            if name:
                view.set_name( name )
                return

            # // Name
            name = get_name_from_first_line( view )

            if name:
                view.set_name( name )
                return

