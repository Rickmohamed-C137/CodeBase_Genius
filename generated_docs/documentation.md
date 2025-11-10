
# Project Documentation

## Summary
- Total Python files: 62
- Total functions/classes: 1571

## Details

### docs\conf.py


### examples\aliases\aliases.py

- **Config**
  - The config in this example only holds aliases.

- **__init__**
  - No documentation found.

- **add_alias**
  - No documentation found.

- **read_config**
  - No documentation found.

- **write_config**
  - No documentation found.

- **AliasedGroup**
  - This subclass of a group supports looking up aliases in a config
    file and with a bit of magic.

- **get_command**
  - No documentation found.

- **resolve_command**
  - No documentation found.

- **read_config**
  - Callback that is used whenever --config is passed.  We use this to
    always load the correct config.  This means that the config is loaded
    even if the group itself never executes so our aliases stay always
    available.

- **cli**
  - An example application that supports aliases.

- **push**
  - Pushes changes.

- **pull**
  - Pulls changes.

- **clone**
  - Clones a repository.

- **commit**
  - Commits pending changes.

- **status**
  - Shows the status.

- **alias**
  - Adds an alias to the specified configuration file.


### examples\colors\colors.py

- **cli**
  - This script prints some colors. It will also automatically remove
    all ANSI styles if data is piped into a file.

    Give it a try!


### examples\completion\completion.py

- **cli**
  - No documentation found.

- **ls**
  - No documentation found.

- **get_env_vars**
  - No documentation found.

- **show_env**
  - No documentation found.

- **group**
  - No documentation found.

- **list_users**
  - No documentation found.

- **select_user**
  - No documentation found.


### examples\complex\complex\cli.py

- **Environment**
  - No documentation found.

- **__init__**
  - No documentation found.

- **log**
  - Logs a message to stderr.

- **vlog**
  - Logs a message to stderr only if verbose is enabled.

- **ComplexCLI**
  - No documentation found.

- **list_commands**
  - No documentation found.

- **get_command**
  - No documentation found.

- **cli**
  - A complex command line interface.


### examples\complex\complex\__init__.py


### examples\complex\complex\commands\cmd_init.py

- **cli**
  - Initializes a repository.


### examples\complex\complex\commands\cmd_status.py

- **cli**
  - Shows file changes in the current working directory.


### examples\complex\complex\commands\__init__.py


### examples\imagepipe\imagepipe.py

- **cli**
  - This script processes a bunch of images through pillow in a unix
    pipe.  One commands feeds into the next.

    Example:

    \b
        imagepipe open -i example01.jpg resize -w 128 display
        imagepipe open -i example02.jpg blur save

- **process_commands**
  - This result callback is invoked with an iterable of all the chained
    subcommands.  As in this example each subcommand returns a function
    we can chain them together to feed one into the other, similar to how
    a pipe on unix works.

- **processor**
  - Helper decorator to rewrite a function so that it returns another
    function from it.

- **new_func**
  - No documentation found.

- **processor**
  - No documentation found.

- **generator**
  - Similar to the :func:`processor` but passes through old values
    unchanged and does not pass through the values as parameter.

- **new_func**
  - No documentation found.

- **copy_filename**
  - No documentation found.

- **open_cmd**
  - Loads one or multiple images for processing.  The input parameter
    can be specified multiple times to load more than one image.

- **save_cmd**
  - Saves all processed images to a series of files.

- **display_cmd**
  - Opens all images in an image viewer.

- **resize_cmd**
  - Resizes an image by fitting it into the box without changing
    the aspect ratio.

- **crop_cmd**
  - Crops an image from all edges.

- **convert_rotation**
  - No documentation found.

- **convert_flip**
  - No documentation found.

- **transpose_cmd**
  - Transposes an image by either rotating or flipping it.

- **blur_cmd**
  - Applies gaussian blur.

- **smoothen_cmd**
  - Applies a smoothening filter.

- **emboss_cmd**
  - Embosses an image.

- **sharpen_cmd**
  - Sharpens an image.

- **paste_cmd**
  - Pastes the second image on the first image and leaves the rest
    unchanged.


### examples\inout\inout.py

- **cli**
  - This script works similar to the Unix `cat` command but it writes
    into a specific file (which could be the standard output as denoted by
    the ``-`` sign).

    \b
    Copy stdin to stdout:
        inout - -

    \b
    Copy foo.txt and bar.txt to stdout:
        inout foo.txt bar.txt -

    \b
    Write stdin into the file foo.txt
        inout - foo.txt


### examples\naval\naval.py

- **cli**
  - Naval Fate.

    This is the docopt example adopted to Click but with some actual
    commands implemented and not just the empty parsing which really
    is not all that interesting.

- **ship**
  - Manages ships.

- **ship_new**
  - Creates a new ship.

- **ship_move**
  - Moves SHIP to the new location X,Y.

- **ship_shoot**
  - Makes SHIP fire to X,Y.

- **mine**
  - Manages mines.

- **mine_set**
  - Sets a mine at a specific coordinate.

- **mine_remove**
  - Removes a mine at a specific coordinate.


### examples\repo\repo.py

- **Repo**
  - No documentation found.

- **__init__**
  - No documentation found.

- **set_config**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **cli**
  - Repo is a command line tool that showcases how to build complex
    command line interfaces with Click.

    This tool is supposed to look like a distributed version control
    system to show how something like this can be structured.

- **clone**
  - Clones a repository.

    This will clone the repository at SRC into the folder DEST.  If DEST
    is not provided this will automatically use the last path component
    of SRC and create that folder.

- **delete**
  - Deletes a repository.

    This will throw away the current repository.

- **setuser**
  - Sets the user credentials.

    This will override the current user config.

- **commit**
  - Commits outstanding changes.

    Commit changes to the given files into the repository.  You will need to
    "repo push" to push up your changes to other repositories.

    If a list of files is omitted, all changes reported by "repo status"
    will be committed.

- **copy**
  - Copies one or multiple files to a new location.  This copies all
    files from SRC to DST.


### examples\termui\termui.py

- **cli**
  - This script showcases different terminal UI helpers in Click.

- **colordemo**
  - Demonstrates ANSI color support.

- **pager**
  - Demonstrates using the pager.

- **progress**
  - Demonstrates the progress bar.

- **process_slowly**
  - No documentation found.

- **filter**
  - No documentation found.

- **show_item**
  - No documentation found.

- **open**
  - Opens a file or URL In the default application.

- **locate**
  - Opens a file or URL In the default application.

- **edit**
  - Opens an editor with some text in it.

- **clear**
  - Clears the entire screen.

- **pause**
  - Waits for the user to press a button.

- **menu**
  - Shows a simple menu.


### examples\validation\validation.py

- **validate_count**
  - No documentation found.

- **URL**
  - No documentation found.

- **convert**
  - No documentation found.

- **cli**
  - Validation.

    This example validates parameters in different ways.  It does it
    through callbacks, through a custom type as well as by validating
    manually in the function.


### src\click\core.py

- **_complete_visible_commands**
  - No documentation found.

- **_check_nested_chain**
  - No documentation found.

- **batch**
  - No documentation found.

- **augment_usage_errors**
  - No documentation found.

- **iter_params_for_processing**
  - No documentation found.

- **sort_key**
  - No documentation found.

- **ParameterSource**
  - This is an :class:`~enum.Enum` that indicates the source of a
    parameter's value.

    Use :meth:`click.Context.get_parameter_source` to get the
    source for a parameter by name.

    .. versionchanged:: 8.0
        Use :class:`~enum.Enum` and drop the ``validate`` method.

    .. versionchanged:: 8.0
        Added the ``PROMPT`` value.

- **Context**
  - The context is a special internal object that holds state relevant
    for the script execution at every single level.  It's normally invisible
    to commands unless they opt-in to getting access to it.

    The context is useful as it can pass internal objects around and can
    control special execution features such as reading data from
    environment variables.

    A context can be used as context manager in which case it will call
    :meth:`close` on teardown.

    :param command: the command class for this context.
    :param parent: the parent context.
    :param info_name: the info name for this invocation.  Generally this
                      is the most descriptive name for the script or
                      command.  For the toplevel script it is usually
                      the name of the script, for commands below it it's
                      the name of the script.
    :param obj: an arbitrary object of user data.
    :param auto_envvar_prefix: the prefix to use for automatic environment
                               variables.  If this is `None` then reading
                               from environment variables is disabled.  This
                               does not affect manually set environment
                               variables which are always read.
    :param default_map: a dictionary (like object) with default values
                        for parameters.
    :param terminal_width: the width of the terminal.  The default is
                           inherit from parent context.  If no context
                           defines the terminal width then auto
                           detection will be applied.
    :param max_content_width: the maximum width for content rendered by
                              Click (this currently only affects help
                              pages).  This defaults to 80 characters if
                              not overridden.  In other words: even if the
                              terminal is larger than that, Click will not
                              format things wider than 80 characters by
                              default.  In addition to that, formatters might
                              add some safety mapping on the right.
    :param resilient_parsing: if this flag is enabled then Click will
                              parse without any interactivity or callback
                              invocation.  Default values will also be
                              ignored.  This is useful for implementing
                              things such as completion support.
    :param allow_extra_args: if this is set to `True` then extra arguments
                             at the end will not raise an error and will be
                             kept on the context.  The default is to inherit
                             from the command.
    :param allow_interspersed_args: if this is set to `False` then options
                                    and arguments cannot be mixed.  The
                                    default is to inherit from the command.
    :param ignore_unknown_options: instructs click to ignore options it does
                                   not know and keeps them for later
                                   processing.
    :param help_option_names: optionally a list of strings that define how
                              the default help parameter is named.  The
                              default is ``['--help']``.
    :param token_normalize_func: an optional function that is used to
                                 normalize tokens (options, choices,
                                 etc.).  This for instance can be used to
                                 implement case insensitive behavior.
    :param color: controls if the terminal supports ANSI colors or not.  The
                  default is autodetection.  This is only needed if ANSI
                  codes are used in texts that Click prints which is by
                  default not the case.  This for instance would affect
                  help output.
    :param show_default: Show the default value for commands. If this
        value is not set, it defaults to the value from the parent
        context. ``Command.show_default`` overrides this default for the
        specific command.

    .. versionchanged:: 8.2
        The ``protected_args`` attribute is deprecated and will be removed in
        Click 9.0. ``args`` will contain remaining unparsed tokens.

    .. versionchanged:: 8.1
        The ``show_default`` parameter is overridden by
        ``Command.show_default``, instead of the other way around.

    .. versionchanged:: 8.0
        The ``show_default`` parameter defaults to the value from the
        parent context.

    .. versionchanged:: 7.1
       Added the ``show_default`` parameter.

    .. versionchanged:: 4.0
        Added the ``color``, ``ignore_unknown_options``, and
        ``max_content_width`` parameters.

    .. versionchanged:: 3.0
        Added the ``allow_extra_args`` and ``allow_interspersed_args``
        parameters.

    .. versionchanged:: 2.0
        Added the ``resilient_parsing``, ``help_option_names``, and
        ``token_normalize_func`` parameters.

- **to**
  - No documentation found.

- **__init__**
  - No documentation found.

- **protected_args**
  - No documentation found.

- **to_info_dict**
  - Gather information that could be useful for a tool generating
        user-facing documentation. This traverses the entire CLI
        structure.

        .. code-block:: python

            with Context(cli) as ctx:
                info = ctx.to_info_dict()

        .. versionadded:: 8.0

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **scope**
  - No documentation found.

- **meta**
  - This is a dictionary which is shared with all the contexts
        that are nested.  It exists so that click utilities can store some
        state here if they need to.  It is however the responsibility of
        that code to manage this dictionary well.

        The keys are supposed to be unique dotted strings.  For instance
        module paths are a good choice for it.  What is stored in there is
        irrelevant for the operation of click.  However what is important is
        that code that places data here adheres to the general semantics of
        the system.

        Example usage::

            LANG_KEY = f'{__name__}.lang'

            def set_language(value):
                ctx = get_current_context()
                ctx.meta[LANG_KEY] = value

            def get_language():
                return get_current_context().meta.get(LANG_KEY, 'en_US')

        .. versionadded:: 5.0

- **make_formatter**
  - Creates the :class:`~click.HelpFormatter` for the help and
        usage output.

        To quickly customize the formatter class used without overriding
        this method, set the :attr:`formatter_class` attribute.

        .. versionchanged:: 8.0
            Added the :attr:`formatter_class` attribute.

- **with_resource**
  - No documentation found.

- **cli**
  - No documentation found.

- **call_on_close**
  - No documentation found.

- **close**
  - Invoke all close callbacks registered with
        :meth:`call_on_close`, and exit all context managers entered
        with :meth:`with_resource`.

- **_close_with_exception_info**
  - No documentation found.

- **command_path**
  - The computed command path.  This is used for the ``usage``
        information on the help page.  It's automatically created by
        combining the info names of the chain of contexts to the root.

- **find_root**
  - Finds the outermost context.

- **find_object**
  - No documentation found.

- **ensure_object**
  - No documentation found.

- **lookup_default**
  - No documentation found.

- **lookup_default**
  - No documentation found.

- **lookup_default**
  - No documentation found.

- **fail**
  - No documentation found.

- **abort**
  - Aborts the script.

- **exit**
  - No documentation found.

- **get_usage**
  - Helper method to get formatted usage string for the current
        context and command.

- **get_help**
  - Helper method to get formatted help page for the current
        context and command.

- **_make_sub_context**
  - No documentation found.

- **invoke**
  - No documentation found.

- **invoke**
  - No documentation found.

- **invoke**
  - No documentation found.

- **forward**
  - No documentation found.

- **set_parameter_source**
  - No documentation found.

- **get_parameter_source**
  - No documentation found.

- **Command**
  - Commands are the basic building block of command line interfaces in
    Click.  A basic command handles command line parsing and might dispatch
    more parsing to commands nested below it.

    :param name: the name of the command to use unless a group overrides it.
    :param context_settings: an optional dictionary with defaults that are
                             passed to the context object.
    :param callback: the callback to invoke.  This is optional.
    :param params: the parameters to register with this command.  This can
                   be either :class:`Option` or :class:`Argument` objects.
    :param help: the help string to use for this command.
    :param epilog: like the help string but it's printed at the end of the
                   help page after everything else.
    :param short_help: the short help to use for this command.  This is
                       shown on the command listing of the parent command.
    :param add_help_option: by default each command registers a ``--help``
                            option.  This can be disabled by this parameter.
    :param no_args_is_help: this controls what happens if no arguments are
                            provided.  This option is disabled by default.
                            If enabled this will add ``--help`` as argument
                            if no arguments are passed
    :param hidden: hide this command from help outputs.
    :param deprecated: If ``True`` or non-empty string, issues a message
                        indicating that the command is deprecated and highlights
                        its deprecation in --help. The message can be customized
                        by using a string as the value.

    .. versionchanged:: 8.2
        This is the base class for all commands, not ``BaseCommand``.
        ``deprecated`` can be set to a string as well to customize the
        deprecation message.

    .. versionchanged:: 8.1
        ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
        all formatting is done when outputting help text, not at init,
        and is done even if not using the ``@command`` decorator.

    .. versionchanged:: 8.0
        Added a ``repr`` showing the command name.

    .. versionchanged:: 7.1
        Added the ``no_args_is_help`` parameter.

    .. versionchanged:: 2.0
        Added the ``context_settings`` parameter.

- **to**
  - No documentation found.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **get_usage**
  - No documentation found.

- **get_params**
  - No documentation found.

- **format_usage**
  - No documentation found.

- **collect_usage_pieces**
  - No documentation found.

- **get_help_option_names**
  - No documentation found.

- **get_help_option**
  - No documentation found.

- **make_parser**
  - No documentation found.

- **get_help**
  - No documentation found.

- **get_short_help_str**
  - No documentation found.

- **format_help**
  - No documentation found.

- **format_help_text**
  - No documentation found.

- **format_options**
  - No documentation found.

- **format_epilog**
  - No documentation found.

- **make_context**
  - No documentation found.

- **used**
  - No documentation found.

- **parse_args**
  - No documentation found.

- **invoke**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **main**
  - No documentation found.

- **main**
  - No documentation found.

- **main**
  - No documentation found.

- **_main_shell_completion**
  - No documentation found.

- **__call__**
  - No documentation found.

- **_FakeSubclassCheck**
  - No documentation found.

- **__subclasscheck__**
  - No documentation found.

- **__instancecheck__**
  - No documentation found.

- **_BaseCommand**
  - .. deprecated:: 8.2
        Will be removed in Click 9.0. Use ``Command`` instead.

- **Group**
  - A group is a command that nests other commands (or more groups).

    :param name: The name of the group command.
    :param commands: Map names to :class:`Command` objects. Can be a list, which
        will use :attr:`Command.name` as the keys.
    :param invoke_without_command: Invoke the group's callback even if a
        subcommand is not given.
    :param no_args_is_help: If no arguments are given, show the group's help and
        exit. Defaults to the opposite of ``invoke_without_command``.
    :param subcommand_metavar: How to represent the subcommand argument in help.
        The default will represent whether ``chain`` is set or not.
    :param chain: Allow passing more than one subcommand argument. After parsing
        a command's arguments, if any arguments remain another command will be
        matched, and so on.
    :param result_callback: A function to call after the group's and
        subcommand's callbacks. The value returned by the subcommand is passed.
        If ``chain`` is enabled, the value will be a list of values returned by
        all the commands. If ``invoke_without_command`` is enabled, the value
        will be the value returned by the group's callback, or an empty list if
        ``chain`` is enabled.
    :param kwargs: Other arguments passed to :class:`Command`.

    .. versionchanged:: 8.0
        The ``commands`` argument can be a list of command objects.

    .. versionchanged:: 8.2
        Merged with and replaces the ``MultiCommand`` base class.

- **will**
  - No documentation found.

- **continue**
  - No documentation found.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **add_command**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **used**
  - No documentation found.

- **and**
  - No documentation found.

- **def**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **used**
  - No documentation found.

- **is**
  - No documentation found.

- **is**
  - No documentation found.

- **def**
  - No documentation found.

- **result_callback**
  - No documentation found.

- **cli**
  - No documentation found.

- **process_result**
  - No documentation found.

- **decorator**
  - No documentation found.

- **function**
  - No documentation found.

- **get_command**
  - No documentation found.

- **list_commands**
  - No documentation found.

- **collect_usage_pieces**
  - No documentation found.

- **format_options**
  - No documentation found.

- **format_commands**
  - No documentation found.

- **parse_args**
  - No documentation found.

- **invoke**
  - No documentation found.

- **_process_result**
  - No documentation found.

- **resolve_command**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **_MultiCommand**
  - .. deprecated:: 8.2
        Will be removed in Click 9.0. Use ``Group`` instead.

- **CommandCollection**
  - A :class:`Group` that looks up subcommands on other groups. If a command
    is not found on this group, each registered source is checked in order.
    Parameters on a source are not added to this group, and a source's callback
    is not invoked when invoking its commands. In other words, this "flattens"
    commands in many groups into this one group.

    :param name: The name of the group command.
    :param sources: A list of :class:`Group` objects to look up commands from.
    :param kwargs: Other arguments passed to :class:`Group`.

    .. versionchanged:: 8.2
        This is a subclass of ``Group``. Commands are looked up first on this
        group, then each of its sources.

- **__init__**
  - No documentation found.

- **add_source**
  - No documentation found.

- **get_command**
  - No documentation found.

- **list_commands**
  - No documentation found.

- **_check_iter**
  - No documentation found.

- **Parameter**
  - No documentation found.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionchanged:: 8.3.0
            Returns ``None`` for the :attr:`default` if it was not set.

        .. versionadded:: 8.0

- **__repr__**
  - No documentation found.

- **_parse_decls**
  - No documentation found.

- **human_readable_name**
  - Returns the human readable name of this parameter.  This is the
        same as the name for options, but the metavar for arguments.

- **make_metavar**
  - No documentation found.

- **get_default**
  - No documentation found.

- **get_default**
  - No documentation found.

- **get_default**
  - No documentation found.

- **add_to_parser**
  - No documentation found.

- **consume_value**
  - No documentation found.

- **type_cast_value**
  - No documentation found.

- **check_iter**
  - No documentation found.

- **convert**
  - No documentation found.

- **convert**
  - No documentation found.

- **convert**
  - No documentation found.

- **value_is_missing**
  - No documentation found.

- **process_value**
  - No documentation found.

- **resolve_envvar_value**
  - No documentation found.

- **value_from_envvar**
  - No documentation found.

- **handle_parse_result**
  - No documentation found.

- **get_help_record**
  - No documentation found.

- **get_usage_pieces**
  - No documentation found.

- **get_error_hint**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **Option**
  - Options are usually optional values on the command line and
    have some extra features that arguments don't have.

    All other parameters are passed onwards to the parameter constructor.

    :param show_default: Show the default value for this option in its
        help text. Values are not shown by default, unless
        :attr:`Context.show_default` is ``True``. If this value is a
        string, it shows that string in parentheses instead of the
        actual value. This is particularly useful for dynamic options.
        For single option boolean flags, the default remains hidden if
        its value is ``False``.
    :param show_envvar: Controls if an environment variable should be
        shown on the help page and error messages.
        Normally, environment variables are not shown.
    :param prompt: If set to ``True`` or a non empty string then the
        user will be prompted for input. If set to ``True`` the prompt
        will be the option name capitalized. A deprecated option cannot be
        prompted.
    :param confirmation_prompt: Prompt a second time to confirm the
        value if it was prompted for. Can be set to a string instead of
        ``True`` to customize the message.
    :param prompt_required: If set to ``False``, the user will be
        prompted for input only when the option was specified as a flag
        without a value.
    :param hide_input: If this is ``True`` then the input on the prompt
        will be hidden from the user. This is useful for password input.
    :param is_flag: forces this option to act as a flag.  The default is
                    auto detection.
    :param flag_value: which value should be used for this flag if it's
                       enabled.  This is set to a boolean automatically if
                       the option string contains a slash to mark two options.
    :param multiple: if this is set to `True` then the argument is accepted
                     multiple times and recorded.  This is similar to ``nargs``
                     in how it works but supports arbitrary number of
                     arguments.
    :param count: this flag makes an option increment an integer.
    :param allow_from_autoenv: if this is enabled then the value of this
                               parameter will be pulled from an environment
                               variable in case a prefix is defined on the
                               context.
    :param help: the help string.
    :param hidden: hide this option from help outputs.
    :param attrs: Other command arguments described in :class:`Parameter`.

    .. versionchanged:: 8.2
        ``envvar`` used with ``flag_value`` will always use the ``flag_value``,
        previously it would use the value of the environment variable.

    .. versionchanged:: 8.1
        Help text indentation is cleaned here instead of only in the
        ``@option`` decorator.

    .. versionchanged:: 8.1
        The ``show_default`` parameter overrides
        ``Context.show_default``.

    .. versionchanged:: 8.1
        The default of a single option boolean flag is not shown if the
        default value is ``False``.

    .. versionchanged:: 8.0.1
        ``type`` is detected from ``flag_value`` if given.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - .. versionchanged:: 8.3.0
            Returns ``None`` for the :attr:`flag_value` if it was not set.

- **get_error_hint**
  - No documentation found.

- **_parse_decls**
  - No documentation found.

- **add_to_parser**
  - No documentation found.

- **get_help_record**
  - No documentation found.

- **_write_opts**
  - No documentation found.

- **get_help_extra**
  - No documentation found.

- **prompt_for_value**
  - No documentation found.

- **resolve_envvar_value**
  - No documentation found.

- **value_from_envvar**
  - No documentation found.

- **consume_value**
  - No documentation found.

- **process_value**
  - No documentation found.

- **Argument**
  - Arguments are positional parameters to a command.  They generally
    provide fewer features than options but can have infinite ``nargs``
    and are required by default.

    All parameters are passed onwards to the constructor of :class:`Parameter`.

- **__init__**
  - No documentation found.

- **human_readable_name**
  - No documentation found.

- **make_metavar**
  - No documentation found.

- **_parse_decls**
  - No documentation found.

- **get_usage_pieces**
  - No documentation found.

- **get_error_hint**
  - No documentation found.

- **add_to_parser**
  - No documentation found.

- **__getattr__**
  - No documentation found.


### src\click\decorators.py

- **pass_context**
  - No documentation found.

- **new_func**
  - No documentation found.

- **pass_obj**
  - No documentation found.

- **new_func**
  - No documentation found.

- **make_pass_decorator**
  - No documentation found.

- **decorator**
  - No documentation found.

- **new_func**
  - No documentation found.

- **decorator**
  - No documentation found.

- **new_func**
  - No documentation found.

- **pass_meta_key**
  - No documentation found.

- **decorator**
  - No documentation found.

- **new_func**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **command**
  - No documentation found.

- **to**
  - No documentation found.

- **decorator**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **group**
  - No documentation found.

- **_param_memo**
  - No documentation found.

- **argument**
  - No documentation found.

- **to**
  - No documentation found.

- **decorator**
  - No documentation found.

- **option**
  - No documentation found.

- **to**
  - No documentation found.

- **decorator**
  - No documentation found.

- **confirmation_option**
  - No documentation found.

- **callback**
  - No documentation found.

- **password_option**
  - No documentation found.

- **version_option**
  - No documentation found.

- **callback**
  - No documentation found.

- **help_option**
  - No documentation found.

- **show_help**
  - No documentation found.


### src\click\exceptions.py

- **_join_param_hints**
  - No documentation found.

- **ClickException**
  - An exception that Click can handle and show to the user.

- **__init__**
  - No documentation found.

- **format_message**
  - No documentation found.

- **__str__**
  - No documentation found.

- **show**
  - No documentation found.

- **UsageError**
  - An internal exception that signals a usage error.  This typically
    aborts any further handling.

    :param message: the error message to display.
    :param ctx: optionally the context that caused this error.  Click will
                fill in the context automatically in some situations.

- **__init__**
  - No documentation found.

- **show**
  - No documentation found.

- **BadParameter**
  - An exception that formats out a standardized error message for a
    bad parameter.  This is useful when thrown from a callback or type as
    Click will attach contextual information to it (for instance, which
    parameter it is).

    .. versionadded:: 2.0

    :param param: the parameter object that caused this error.  This can
                  be left out, and Click will attach this info itself
                  if possible.
    :param param_hint: a string that shows up as parameter name.  This
                       can be used as alternative to `param` in cases
                       where custom validation should happen.  If it is
                       a string it's used as such, if it's a list then
                       each item is quoted and separated.

- **__init__**
  - No documentation found.

- **format_message**
  - No documentation found.

- **MissingParameter**
  - Raised if click required an option or argument but it was not
    provided when invoking the script.

    .. versionadded:: 4.0

    :param param_type: a string that indicates the type of the parameter.
                       The default is to inherit the parameter type from
                       the given `param`.  Valid values are ``'parameter'``,
                       ``'option'`` or ``'argument'``.

- **__init__**
  - No documentation found.

- **format_message**
  - No documentation found.

- **__str__**
  - No documentation found.

- **NoSuchOption**
  - Raised if click attempted to handle an option that does not
    exist.

    .. versionadded:: 4.0

- **__init__**
  - No documentation found.

- **format_message**
  - No documentation found.

- **BadOptionUsage**
  - Raised if an option is generally supplied but the use of the option
    was incorrect.  This is for instance raised if the number of arguments
    for an option is not correct.

    .. versionadded:: 4.0

    :param option_name: the name of the option being used incorrectly.

- **__init__**
  - No documentation found.

- **BadArgumentUsage**
  - Raised if an argument is generally supplied but the use of the argument
    was incorrect.  This is for instance raised if the number of values
    for an argument is not correct.

    .. versionadded:: 6.0

- **NoArgsIsHelpError**
  - No documentation found.

- **__init__**
  - No documentation found.

- **show**
  - No documentation found.

- **FileError**
  - Raised if a file cannot be opened.

- **__init__**
  - No documentation found.

- **format_message**
  - No documentation found.

- **Abort**
  - An internal signalling exception that signals Click to abort.

- **Exit**
  - An exception that indicates that the application should exit with some
    status code.

    :param code: the status code to exit with.

- **__init__**
  - No documentation found.


### src\click\formatting.py

- **measure_table**
  - No documentation found.

- **iter_rows**
  - No documentation found.

- **wrap_text**
  - No documentation found.

- **_flush_par**
  - No documentation found.

- **HelpFormatter**
  - This class helps with formatting text-based help pages.  It's
    usually just needed for very special internal cases, but it's also
    exposed so that developers can write their own fancy outputs.

    At present, it always writes into memory.

    :param indent_increment: the additional increment for each level.
    :param width: the width for the text.  This defaults to the terminal
                  width clamped to a maximum of 78.

- **__init__**
  - No documentation found.

- **write**
  - No documentation found.

- **indent**
  - Increases the indentation.

- **dedent**
  - Decreases the indentation.

- **write_usage**
  - No documentation found.

- **write_heading**
  - No documentation found.

- **write_paragraph**
  - Writes a paragraph into the buffer.

- **write_text**
  - No documentation found.

- **write_dl**
  - No documentation found.

- **section**
  - No documentation found.

- **indentation**
  - A context manager that increases the indentation.

- **getvalue**
  - Returns the buffer contents.

- **join_options**
  - No documentation found.


### src\click\globals.py

- **get_current_context**
  - No documentation found.

- **get_current_context**
  - No documentation found.

- **get_current_context**
  - No documentation found.

- **push_context**
  - No documentation found.

- **pop_context**
  - Removes the top level from the stack.

- **resolve_color_default**
  - No documentation found.


### src\click\parser.py

- **_unpack_args**
  - No documentation found.

- **_fetch**
  - No documentation found.

- **_split_opt**
  - No documentation found.

- **_normalize_opt**
  - No documentation found.

- **_Option**
  - No documentation found.

- **__init__**
  - No documentation found.

- **takes_value**
  - No documentation found.

- **process**
  - No documentation found.

- **_Argument**
  - No documentation found.

- **__init__**
  - No documentation found.

- **process**
  - No documentation found.

- **_ParsingState**
  - No documentation found.

- **__init__**
  - No documentation found.

- **_OptionParser**
  - The option parser is an internal class that is ultimately used to
    parse options and arguments.  It's modelled after optparse and brings
    a similar but vastly simplified API.  It should generally not be used
    directly as the high level Click classes wrap it for you.

    It's not nearly as extensible as optparse or argparse as it does not
    implement features that are implemented on a higher level (such as
    types or defaults).

    :param ctx: optionally the :class:`~click.Context` where this parser
                should go with.

    .. deprecated:: 8.2
        Will be removed in Click 9.0.

- **__init__**
  - No documentation found.

- **add_option**
  - No documentation found.

- **add_argument**
  - No documentation found.

- **parse_args**
  - No documentation found.

- **_process_args_for_args**
  - No documentation found.

- **_process_args_for_options**
  - No documentation found.

- **_match_long_opt**
  - No documentation found.

- **_match_short_opt**
  - No documentation found.

- **_get_value_from_state**
  - No documentation found.

- **_process_opts**
  - No documentation found.

- **__getattr__**
  - No documentation found.


### src\click\shell_completion.py

- **shell_complete**
  - No documentation found.

- **CompletionItem**
  - Represents a completion value and metadata about the value. The
    default metadata is ``type`` to indicate special shell handling,
    and ``help`` if a shell supports showing a help string next to the
    value.

    Arbitrary parameters can be passed when creating the object, and
    accessed using ``item.attr``. If an attribute wasn't passed,
    accessing it returns ``None``.

    :param value: The completion suggestion.
    :param type: Tells the shell script to provide special completion
        support for the type. Click uses ``"dir"`` and ``"file"``.
    :param help: String shown next to the value if supported.
    :param kwargs: Arbitrary metadata. The built-in implementations
        don't use this, but custom type completions paired with custom
        shell support could use it.

- **__init__**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **ShellComplete**
  - Base class for providing shell completion support. A subclass for
    a given shell will override attributes and methods to implement the
    completion instructions (``source`` and ``complete``).

    :param cli: Command being called.
    :param prog_name: Name of the executable in the shell.
    :param complete_var: Name of the environment variable that holds
        the completion instruction.

    .. versionadded:: 8.0

- **__init__**
  - No documentation found.

- **func_name**
  - The name of the shell function defined by the completion
        script.

- **source_vars**
  - Vars for formatting :attr:`source_template`.

        By default this provides ``complete_func``, ``complete_var``,
        and ``prog_name``.

- **source**
  - Produce the shell script that defines the completion
        function. By default this ``%``-style formats
        :attr:`source_template` with the dict returned by
        :meth:`source_vars`.

- **get_completion_args**
  - Use the env vars defined by the shell script to return a
        tuple of ``args, incomplete``. This must be implemented by
        subclasses.

- **get_completions**
  - No documentation found.

- **format_completion**
  - No documentation found.

- **complete**
  - Produce the completion data to send back to the shell.

        By default this calls :meth:`get_completion_args`, gets the
        completions, then calls :meth:`format_completion` for each
        completion.

- **BashComplete**
  - Shell completion for Bash.

- **_check_version**
  - No documentation found.

- **source**
  - No documentation found.

- **get_completion_args**
  - No documentation found.

- **format_completion**
  - No documentation found.

- **ZshComplete**
  - Shell completion for Zsh.

- **get_completion_args**
  - No documentation found.

- **format_completion**
  - No documentation found.

- **FishComplete**
  - Shell completion for Fish.

- **get_completion_args**
  - No documentation found.

- **format_completion**
  - No documentation found.

- **add_completion_class**
  - No documentation found.

- **under**
  - No documentation found.

- **that**
  - No documentation found.

- **under**
  - No documentation found.

- **get_completion_class**
  - No documentation found.

- **by**
  - No documentation found.

- **is**
  - No documentation found.

- **_is_incomplete_argument**
  - No documentation found.

- **_start_of_option**
  - No documentation found.

- **_is_incomplete_option**
  - No documentation found.

- **_resolve_context**
  - No documentation found.

- **_resolve_incomplete**
  - No documentation found.


### src\click\termui.py

- **hidden_prompt_func**
  - No documentation found.

- **_build_prompt**
  - No documentation found.

- **_format_default**
  - No documentation found.

- **prompt**
  - No documentation found.

- **prompt_func**
  - No documentation found.

- **confirm**
  - No documentation found.

- **echo_via_pager**
  - No documentation found.

- **progressbar**
  - No documentation found.

- **progressbar**
  - No documentation found.

- **progressbar**
  - No documentation found.

- **object**
  - No documentation found.

- **clear**
  - Clears the terminal screen.  This will have the effect of clearing
    the whole visible space of the terminal and moving the cursor to the
    top left.  This does not do anything if not connected to a terminal.

    .. versionadded:: 2.0

- **_interpret_color**
  - No documentation found.

- **style**
  - No documentation found.

- **unstyle**
  - No documentation found.

- **secho**
  - No documentation found.

- **edit**
  - No documentation found.

- **edit**
  - No documentation found.

- **edit**
  - No documentation found.

- **edit**
  - No documentation found.

- **launch**
  - No documentation found.

- **getchar**
  - No documentation found.

- **raw_terminal**
  - No documentation found.

- **pause**
  - No documentation found.


### src\click\testing.py

- **EchoingStdin**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **_echo**
  - No documentation found.

- **read**
  - No documentation found.

- **read1**
  - No documentation found.

- **readline**
  - No documentation found.

- **readlines**
  - No documentation found.

- **__iter__**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **_pause_echo**
  - No documentation found.

- **BytesIOCopy**
  - Patch ``io.BytesIO`` to let the written stream be copied to another.

    .. versionadded:: 8.2

- **__init__**
  - No documentation found.

- **flush**
  - No documentation found.

- **write**
  - No documentation found.

- **StreamMixer**
  - Mixes `<stdout>` and `<stderr>` streams.

    The result is available in the ``output`` attribute.

    .. versionadded:: 8.2

- **__init__**
  - No documentation found.

- **__del__**
  - Guarantee that embedded file-like objects are closed in a
        predictable order, protecting against races between
        self.output being closed and other streams being flushed on close

        .. versionadded:: 8.2.2

- **_NamedTextIOWrapper**
  - No documentation found.

- **__init__**
  - No documentation found.

- **name**
  - No documentation found.

- **mode**
  - No documentation found.

- **make_input_stream**
  - No documentation found.

- **Result**
  - Holds the captured result of an invoked CLI script.

    :param runner: The runner that created the result
    :param stdout_bytes: The standard output as bytes.
    :param stderr_bytes: The standard error as bytes.
    :param output_bytes: A mix of ``stdout_bytes`` and ``stderr_bytes``, as the
        user would see  it in its terminal.
    :param return_value: The value returned from the invoked command.
    :param exit_code: The exit code as integer.
    :param exception: The exception that happened if one did.
    :param exc_info: Exception information (exception type, exception instance,
        traceback type).

    .. versionchanged:: 8.2
        ``stderr_bytes`` no longer optional, ``output_bytes`` introduced and
        ``mix_stderr`` has been removed.

    .. versionadded:: 8.0
        Added ``return_value``.

- **__init__**
  - No documentation found.

- **output**
  - The terminal output as unicode string, as the user would see it.

        .. versionchanged:: 8.2
            No longer a proxy for ``self.stdout``. Now has its own independent stream
            that is mixing `<stdout>` and `<stderr>`, in the order they were written.

- **stdout**
  - The standard output as unicode string.

- **stderr**
  - The standard error as unicode string.

        .. versionchanged:: 8.2
            No longer raise an exception, always returns the `<stderr>` string.

- **__repr__**
  - No documentation found.

- **CliRunner**
  - The CLI runner provides functionality to invoke a Click command line
    script for unittesting purposes in a isolated environment.  This only
    works in single-threaded systems without any concurrency as it changes the
    global interpreter state.

    :param charset: the character set for the input and output data.
    :param env: a dictionary with environment variables for overriding.
    :param echo_stdin: if this is set to `True`, then reading from `<stdin>` writes
                       to `<stdout>`.  This is useful for showing examples in
                       some circumstances.  Note that regular prompts
                       will automatically echo the input.
    :param catch_exceptions: Whether to catch any exceptions other than
                             ``SystemExit`` when running :meth:`~CliRunner.invoke`.

    .. versionchanged:: 8.2
        Added the ``catch_exceptions`` parameter.

    .. versionchanged:: 8.2
        ``mix_stderr`` parameter has been removed.

- **__init__**
  - No documentation found.

- **get_default_prog_name**
  - No documentation found.

- **make_env**
  - No documentation found.

- **isolation**
  - No documentation found.

- **visible_input**
  - No documentation found.

- **hidden_input**
  - No documentation found.

- **_getchar**
  - No documentation found.

- **should_strip_ansi**
  - No documentation found.

- **invoke**
  - No documentation found.

- **isolated_filesystem**
  - No documentation found.


### src\click\types.py

- **ParamType**
  - Represents the type of a parameter. Validates and converts values
    from the command line or Python into the correct type.

    To implement a custom type, subclass and implement at least the
    following:

    -   The :attr:`name` class attribute must be set.
    -   Calling an instance of the type with ``None`` must return
        ``None``. This is already implemented by default.
    -   :meth:`convert` must convert string values to the correct type.
    -   :meth:`convert` must accept values that are already the correct
        type.
    -   It must be able to convert a value if the ``ctx`` and ``param``
        arguments are ``None``. This can occur when converting prompt
        input.

- **to_info_dict**
  - Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionadded:: 8.0

- **name**
  - No documentation found.

- **__call__**
  - No documentation found.

- **get_metavar**
  - No documentation found.

- **get_missing_message**
  - No documentation found.

- **convert**
  - No documentation found.

- **split_envvar_value**
  - No documentation found.

- **fail**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **CompositeParamType**
  - No documentation found.

- **arity**
  - No documentation found.

- **FuncParamType**
  - No documentation found.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **convert**
  - No documentation found.

- **UnprocessedParamType**
  - No documentation found.

- **convert**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **StringParamType**
  - No documentation found.

- **convert**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **Choice**
  - The choice type allows a value to be checked against a fixed set
    of supported values.

    You may pass any iterable value which will be converted to a tuple
    and thus will only be iterated once.

    The resulting value will always be one of the originally passed choices.
    See :meth:`normalize_choice` for more info on the mapping of strings
    to choices. See :ref:`choice-opts` for an example.

    :param case_sensitive: Set to false to make choices case
        insensitive. Defaults to true.

    .. versionchanged:: 8.2.0
        Non-``str`` ``choices`` are now supported. It can additionally be any
        iterable. Before you were not recommended to pass anything but a list or
        tuple.

    .. versionadded:: 8.2.0
        Choice normalization can be overridden via :meth:`normalize_choice`.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **_normalized_mapping**
  - No documentation found.

- **normalize_choice**
  - No documentation found.

- **get_metavar**
  - No documentation found.

- **get_missing_message**
  - No documentation found.

- **convert**
  - No documentation found.

- **get_invalid_choice_message**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **DateTime**
  - The DateTime type converts date strings into `datetime` objects.

    The format strings which are checked are configurable, but default to some
    common (non-timezone aware) ISO 8601 formats.

    When specifying *DateTime* formats, you should only pass a list or a tuple.
    Other iterables, like generators, may lead to surprising results.

    The format strings are processed using ``datetime.strptime``, and this
    consequently defines the format strings which are allowed.

    Parsing is tried using each format, in order, and the first format which
    parses successfully is used.

    :param formats: A list or tuple of date format strings, in the order in
                    which they should be tried. Defaults to
                    ``'%Y-%m-%d'``, ``'%Y-%m-%dT%H:%M:%S'``,
                    ``'%Y-%m-%d %H:%M:%S'``.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **get_metavar**
  - No documentation found.

- **_try_to_convert_date**
  - No documentation found.

- **convert**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **_NumberParamTypeBase**
  - No documentation found.

- **convert**
  - No documentation found.

- **_NumberRangeBase**
  - No documentation found.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **convert**
  - No documentation found.

- **_clamp**
  - No documentation found.

- **_describe_range**
  - Describe the range for use in help text.

- **__repr__**
  - No documentation found.

- **IntParamType**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **IntRange**
  - Restrict an :data:`click.INT` value to a range of accepted
    values. See :ref:`ranges`.

    If ``min`` or ``max`` are not passed, any value is accepted in that
    direction. If ``min_open`` or ``max_open`` are enabled, the
    corresponding boundary is not included in the range.

    If ``clamp`` is enabled, a value outside the range is clamped to the
    boundary instead of failing.

    .. versionchanged:: 8.0
        Added the ``min_open`` and ``max_open`` parameters.

- **_clamp**
  - No documentation found.

- **FloatParamType**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **FloatRange**
  - Restrict a :data:`click.FLOAT` value to a range of accepted
    values. See :ref:`ranges`.

    If ``min`` or ``max`` are not passed, any value is accepted in that
    direction. If ``min_open`` or ``max_open`` are enabled, the
    corresponding boundary is not included in the range.

    If ``clamp`` is enabled, a value outside the range is clamped to the
    boundary instead of failing. This is not supported if either
    boundary is marked ``open``.

    .. versionchanged:: 8.0
        Added the ``min_open`` and ``max_open`` parameters.

- **__init__**
  - No documentation found.

- **_clamp**
  - No documentation found.

- **BoolParamType**
  - No documentation found.

- **str_to_bool**
  - No documentation found.

- **convert**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **UUIDParameterType**
  - No documentation found.

- **convert**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **File**
  - Declares a parameter to be a file for reading or writing.  The file
    is automatically closed once the context tears down (after the command
    finished working).

    Files can be opened for reading or writing.  The special value ``-``
    indicates stdin or stdout depending on the mode.

    By default, the file is opened for reading text data, but it can also be
    opened in binary mode or for writing.  The encoding parameter can be used
    to force a specific encoding.

    The `lazy` flag controls if the file should be opened immediately or upon
    first IO. The default is to be non-lazy for standard input and output
    streams as well as files opened for reading, `lazy` otherwise. When opening a
    file lazily for reading, it is still opened temporarily for validation, but
    will not be held open until first IO. lazy is mainly useful when opening
    for writing to avoid creating the file until it is needed.

    Files can also be opened atomically in which case all writes go into a
    separate file in the same folder and upon completion the file will
    be moved over to the original location.  This is useful if a file
    regularly read by other users is modified.

    See :ref:`file-args` for more information.

    .. versionchanged:: 2.0
        Added the ``atomic`` parameter.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **resolve_lazy_flag**
  - No documentation found.

- **convert**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **_is_file_like**
  - No documentation found.

- **Path**
  - The ``Path`` type is similar to the :class:`File` type, but
    returns the filename instead of an open file. Various checks can be
    enabled to validate the type of file and permissions.

    :param exists: The file or directory needs to exist for the value to
        be valid. If this is not set to ``True``, and the file does not
        exist, then all further checks are silently skipped.
    :param file_okay: Allow a file as a value.
    :param dir_okay: Allow a directory as a value.
    :param readable: if true, a readable check is performed.
    :param writable: if true, a writable check is performed.
    :param executable: if true, an executable check is performed.
    :param resolve_path: Make the value absolute and resolve any
        symlinks. A ``~`` is not expanded, as this is supposed to be
        done by the shell only.
    :param allow_dash: Allow a single dash as a value, which indicates
        a standard stream (but does not open it). Use
        :func:`~click.open_file` to handle opening this value.
    :param path_type: Convert the incoming path value to this type. If
        ``None``, keep Python's default, which is ``str``. Useful to
        convert to :class:`pathlib.Path`.

    .. versionchanged:: 8.1
        Added the ``executable`` parameter.

    .. versionchanged:: 8.0
        Allow passing ``path_type=pathlib.Path``.

    .. versionchanged:: 6.0
        Added the ``allow_dash`` parameter.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **coerce_path_result**
  - No documentation found.

- **convert**
  - No documentation found.

- **shell_complete**
  - No documentation found.

- **Tuple**
  - The default behavior of Click is to apply a type on a value directly.
    This works well in most cases, except for when `nargs` is set to a fixed
    count and different types should be used for different items.  In this
    case the :class:`Tuple` type can be used.  This type can only be used
    if `nargs` is set to a fixed number.

    For more information see :ref:`tuple-type`.

    This can be selected by using a Python tuple literal as a type.

    :param types: a list of types that should be used for the tuple items.

- **__init__**
  - No documentation found.

- **to_info_dict**
  - No documentation found.

- **name**
  - No documentation found.

- **arity**
  - No documentation found.

- **convert**
  - No documentation found.

- **convert_type**
  - No documentation found.

- **fails**
  - No documentation found.

- **OptionHelpExtra**
  - No documentation found.


### src\click\utils.py

- **_posixify**
  - No documentation found.

- **safecall**
  - No documentation found.

- **wrapper**
  - No documentation found.

- **make_str**
  - No documentation found.

- **make_default_short_help**
  - No documentation found.

- **LazyFile**
  - A lazy file works like a regular file but it does not fully open
    the file but it does perform some basic checks early to see if the
    filename parameter does make sense.  This is useful for safely opening
    files for writing.

- **__init__**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **open**
  - Opens the file if it's not yet open.  This call might fail with
        a :exc:`FileError`.  Not handling this error will produce an error
        that Click shows.

- **close**
  - Closes the underlying file, no matter what.

- **close_intelligently**
  - This function only closes the file if it was opened by the lazy
        file wrapper.  For instance this will never close stdin.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **__iter__**
  - No documentation found.

- **KeepOpenFile**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **__iter__**
  - No documentation found.

- **echo**
  - No documentation found.

- **get_binary_stream**
  - No documentation found.

- **get_text_stream**
  - No documentation found.

- **open_file**
  - No documentation found.

- **format_filename**
  - No documentation found.

- **get_app_dir**
  - No documentation found.

- **PacifyFlushWrapper**
  - This wrapper is used to catch and suppress BrokenPipeErrors resulting
    from ``.flush()`` being called on broken pipe during the shutdown/final-GC
    of the Python interpreter. Notably ``.flush()`` is always called on
    ``sys.stdout`` and ``sys.stderr``. So as to have minimal impact on any
    other cleanup code, and the case where the underlying file is not a broken
    pipe, all calls and attributes are proxied.

- **__init__**
  - No documentation found.

- **flush**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **_detect_program_name**
  - No documentation found.

- **_expand_args**
  - No documentation found.


### src\click\_compat.py

- **_make_text_stream**
  - No documentation found.

- **is_ascii_encoding**
  - No documentation found.

- **get_best_encoding**
  - No documentation found.

- **_NonClosingTextIOWrapper**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__del__**
  - No documentation found.

- **isatty**
  - No documentation found.

- **_FixupStream**
  - The new io interface needs more from streams than streams
    traditionally implement.  As such, this fix-up code is necessary in
    some circumstances.

    The forcing of readable and writable flags are there because some tools
    put badly patched objects on sys (one such offender are certain version
    of jupyter notebook).

- **__init__**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **read1**
  - No documentation found.

- **readable**
  - No documentation found.

- **writable**
  - No documentation found.

- **seekable**
  - No documentation found.

- **_is_binary_reader**
  - No documentation found.

- **_is_binary_writer**
  - No documentation found.

- **_find_binary_reader**
  - No documentation found.

- **_find_binary_writer**
  - No documentation found.

- **_stream_is_misconfigured**
  - No documentation found.

- **_is_compat_stream_attr**
  - No documentation found.

- **_is_compatible_text_stream**
  - No documentation found.

- **_force_correct_text_stream**
  - No documentation found.

- **_force_correct_text_reader**
  - No documentation found.

- **_force_correct_text_writer**
  - No documentation found.

- **get_binary_stdin**
  - No documentation found.

- **get_binary_stdout**
  - No documentation found.

- **get_binary_stderr**
  - No documentation found.

- **get_text_stdin**
  - No documentation found.

- **get_text_stdout**
  - No documentation found.

- **get_text_stderr**
  - No documentation found.

- **_wrap_io_open**
  - No documentation found.

- **open_stream**
  - No documentation found.

- **_AtomicFile**
  - No documentation found.

- **__init__**
  - No documentation found.

- **name**
  - No documentation found.

- **close**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **strip_ansi**
  - No documentation found.

- **_is_jupyter_kernel_output**
  - No documentation found.

- **should_strip_ansi**
  - No documentation found.

- **_get_argv_encoding**
  - No documentation found.

- **auto_wrap_for_ansi**
  - No documentation found.

- **_safe_write**
  - No documentation found.

- **_get_argv_encoding**
  - No documentation found.

- **_get_windows_console_stream**
  - No documentation found.

- **term_len**
  - No documentation found.

- **isatty**
  - No documentation found.

- **_make_cached_stream_func**
  - No documentation found.

- **func**
  - No documentation found.


### src\click\_termui_impl.py

- **ProgressBar**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **__iter__**
  - No documentation found.

- **__next__**
  - No documentation found.

- **render_finish**
  - No documentation found.

- **pct**
  - No documentation found.

- **time_per_iteration**
  - No documentation found.

- **eta**
  - No documentation found.

- **format_eta**
  - No documentation found.

- **format_pos**
  - No documentation found.

- **format_pct**
  - No documentation found.

- **format_bar**
  - No documentation found.

- **format_progress_line**
  - No documentation found.

- **render_progress**
  - No documentation found.

- **make_step**
  - No documentation found.

- **update**
  - No documentation found.

- **finish**
  - No documentation found.

- **generator**
  - Return a generator which yields the items added to the bar
        during construction, and updates the progress bar *after* the
        yielded block returns.

- **pager**
  - No documentation found.

- **_pipepager**
  - No documentation found.

- **_tempfilepager**
  - No documentation found.

- **_nullpager**
  - No documentation found.

- **Editor**
  - No documentation found.

- **__init__**
  - No documentation found.

- **get_editor**
  - No documentation found.

- **edit_files**
  - No documentation found.

- **edit**
  - No documentation found.

- **edit**
  - No documentation found.

- **edit**
  - No documentation found.

- **open_url**
  - No documentation found.

- **_unquote_file**
  - No documentation found.

- **_translate_ch_to_exc**
  - No documentation found.

- **raw_terminal**
  - No documentation found.

- **getchar**
  - No documentation found.

- **raw_terminal**
  - No documentation found.

- **getchar**
  - No documentation found.


### src\click\_textwrap.py

- **TextWrapper**
  - No documentation found.

- **_handle_long_word**
  - No documentation found.

- **extra_indent**
  - No documentation found.

- **indent_only**
  - No documentation found.


### src\click\_utils.py

- **Sentinel**
  - Enum used to define sentinel values.

    .. seealso::

        `PEP 661 - Sentinel Values <https://peps.python.org/pep-0661/>`_.

- **__repr__**
  - No documentation found.


### src\click\_winconsole.py

- **Py_buffer**
  - No documentation found.

- **get_buffer**
  - No documentation found.

- **_WindowsConsoleRawIOBase**
  - No documentation found.

- **__init__**
  - No documentation found.

- **isatty**
  - No documentation found.

- **_WindowsConsoleReader**
  - No documentation found.

- **readable**
  - No documentation found.

- **readinto**
  - No documentation found.

- **_WindowsConsoleWriter**
  - No documentation found.

- **writable**
  - No documentation found.

- **_get_error_message**
  - No documentation found.

- **write**
  - No documentation found.

- **ConsoleStream**
  - No documentation found.

- **__init__**
  - No documentation found.

- **name**
  - No documentation found.

- **write**
  - No documentation found.

- **writelines**
  - No documentation found.

- **__getattr__**
  - No documentation found.

- **isatty**
  - No documentation found.

- **__repr__**
  - No documentation found.

- **_get_text_stdin**
  - No documentation found.

- **_get_text_stdout**
  - No documentation found.

- **_get_text_stderr**
  - No documentation found.

- **_is_console**
  - No documentation found.

- **_get_windows_console_stream**
  - No documentation found.


### src\click\__init__.py

- **__getattr__**
  - No documentation found.


### tests\conftest.py

- **runner**
  - No documentation found.


### tests\test_arguments.py

- **test_nargs_star**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_nargs_tup**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_nargs_tup_composite**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_nargs_mismatch_with_tuple_type**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_nargs_err**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_bytes_args**
  - No documentation found.

- **from_bytes**
  - No documentation found.

- **test_file_args**
  - No documentation found.

- **inout**
  - No documentation found.

- **test_path_allow_dash**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_file_atomics**
  - No documentation found.

- **inout**
  - No documentation found.

- **test_stdout_default**
  - No documentation found.

- **inout**
  - No documentation found.

- **test_nargs_envvar**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_nargs_envvar_only_if_values_empty**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_empty_nargs**
  - No documentation found.

- **cmd**
  - No documentation found.

- **cmd2**
  - No documentation found.

- **test_missing_arg**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_required_argument**
  - Test how a required argument is processing the provided values.

- **test_implicit_non_required**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_usage**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_warning**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_required**
  - No documentation found.

- **test_eat_options**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_nargs_star_ordering**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_nargs_specified_plus_star_ordering**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_good_defaults_for_nargs**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_bad_defaults_for_nargs**
  - Some defaults are not valid when nargs is set.

- **cmd**
  - No documentation found.

- **test_multiple_param_decls_not_allowed**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_multiple_not_allowed**
  - No documentation found.

- **test_subcommand_help**
  - No documentation found.

- **cli**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_nested_subcommand_help**
  - No documentation found.

- **cli**
  - No documentation found.

- **cmd**
  - No documentation found.

- **subcmd**
  - No documentation found.

- **test_when_argument_decorator_is_used_multiple_times_cls_is_preserved**
  - No documentation found.

- **CustomArgument**
  - No documentation found.

- **foo**
  - No documentation found.

- **bar**
  - No documentation found.

- **test_duplicate_names_warning**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_argument_custom_class_can_override_type_cast_value_and_never_sees_unset**
  - Test that overriding type_cast_value is supported

    In particular, the argument is never passed an UNSET sentinel value.

- **CustomArgument**
  - No documentation found.

- **type_cast_value**
  - No documentation found.

- **cmd**
  - No documentation found.


### tests\test_basic.py

- **test_basic_functionality**
  - No documentation found.

- **cli**
  - Hello World!

- **test_repr**
  - No documentation found.

- **command**
  - No documentation found.

- **group**
  - No documentation found.

- **subcommand**
  - No documentation found.

- **test_return_values**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_basic_group**
  - No documentation found.

- **cli**
  - This is the root.

- **subcommand**
  - This is a subcommand.

- **test_group_commands_dict**
  - A Group can be built with a dict of commands.

- **sub**
  - No documentation found.

- **test_group_from_list**
  - A Group can be built with a list of commands.

- **sub**
  - No documentation found.

- **test_string_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_int_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_uuid_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_float_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_boolean_switch**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_boolean_flag**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_boolean_conversion**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_flag_value_dual_options**
  - Check how default is processed when options compete for the same variable name.

    Covers the regression reported in
    https://github.com/pallets/click/issues/3024#issuecomment-3146199461

- **cli**
  - No documentation found.

- **test_file_option**
  - No documentation found.

- **input**
  - No documentation found.

- **output**
  - No documentation found.

- **test_file_lazy_mode**
  - No documentation found.

- **input**
  - No documentation found.

- **output**
  - No documentation found.

- **input_non_lazy**
  - No documentation found.

- **test_path_option**
  - No documentation found.

- **write_to_dir**
  - No documentation found.

- **showtype**
  - No documentation found.

- **exists**
  - No documentation found.

- **test_choice_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choice_argument**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choice_argument_enum**
  - No documentation found.

- **MyEnum**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choice_argument_custom_type**
  - No documentation found.

- **MyClass**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__str__**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choice_argument_none**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_datetime_option_default**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_datetime_option_custom**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_required_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_evaluation_order**
  - No documentation found.

- **memo**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_hidden_option**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_hidden_command**
  - No documentation found.

- **cli**
  - No documentation found.

- **nope**
  - No documentation found.

- **test_hidden_group**
  - No documentation found.

- **cli**
  - No documentation found.

- **subgroup**
  - No documentation found.

- **nope**
  - No documentation found.

- **test_summary_line**
  - No documentation found.

- **cli**
  - No documentation found.

- **cmd**
  - Summary line without period

        Here is a sentence. And here too.

- **test_help_invalid_default**
  - No documentation found.


### tests\test_chain.py

- **debug**
  - No documentation found.

- **test_basic_chaining**
  - No documentation found.

- **cli**
  - No documentation found.

- **sdist**
  - No documentation found.

- **bdist**
  - No documentation found.

- **test_chaining_help**
  - No documentation found.

- **cli**
  - ROOT HELP

- **sdist**
  - SDIST HELP

- **bdist**
  - BDIST HELP

- **test_chaining_with_options**
  - No documentation found.

- **cli**
  - No documentation found.

- **sdist**
  - No documentation found.

- **bdist**
  - No documentation found.

- **test_no_command_result_callback**
  - When a group has ``invoke_without_command=True``, the result
    callback is always invoked. A regular group invokes it with
    its return value, a chained group with ``[]``.

- **cli**
  - No documentation found.

- **process_result**
  - No documentation found.

- **test_chaining_with_arguments**
  - No documentation found.

- **cli**
  - No documentation found.

- **sdist**
  - No documentation found.

- **bdist**
  - No documentation found.

- **test_pipeline**
  - No documentation found.

- **cli**
  - No documentation found.

- **process_pipeline**
  - No documentation found.

- **make_uppercase**
  - No documentation found.

- **processor**
  - No documentation found.

- **make_strip**
  - No documentation found.

- **processor**
  - No documentation found.

- **test_args_and_chain**
  - No documentation found.

- **cli**
  - No documentation found.

- **a**
  - No documentation found.

- **b**
  - No documentation found.

- **c**
  - No documentation found.

- **test_group_arg_behavior**
  - No documentation found.

- **bad_cli**
  - No documentation found.

- **bad_cli2**
  - No documentation found.

- **cli**
  - No documentation found.

- **a**
  - No documentation found.

- **test_group_chaining**
  - No documentation found.

- **cli**
  - No documentation found.

- **l1a**
  - No documentation found.

- **l2a**
  - No documentation found.

- **l2b**
  - No documentation found.

- **l1b**
  - No documentation found.


### tests\test_commands.py

- **test_other_command_invoke**
  - No documentation found.

- **cli**
  - No documentation found.

- **other_cmd**
  - No documentation found.

- **test_other_command_forward**
  - No documentation found.

- **test**
  - No documentation found.

- **dist**
  - No documentation found.

- **test_forwarded_params_consistency**
  - No documentation found.

- **first**
  - No documentation found.

- **second**
  - No documentation found.

- **test_auto_shorthelp**
  - No documentation found.

- **cli**
  - No documentation found.

- **short**
  - This is a short text.

- **special_chars**
  - Login and store the token in ~/.netrc.

- **long**
  - This is a long text that is too long to show as short help
        and will be truncated instead.

- **test_command_no_args_is_help**
  - No documentation found.

- **test_default_maps**
  - No documentation found.

- **cli**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_group_with_args**
  - No documentation found.

- **cli**
  - No documentation found.

- **move**
  - No documentation found.

- **test_custom_parser**
  - No documentation found.

- **cli**
  - No documentation found.

- **OptParseCommand**
  - No documentation found.

- **__init__**
  - No documentation found.

- **parse_args**
  - No documentation found.

- **get_usage**
  - No documentation found.

- **get_help**
  - No documentation found.

- **invoke**
  - No documentation found.

- **test_callback**
  - No documentation found.

- **test_object_propagation**
  - No documentation found.

- **cli**
  - No documentation found.

- **sync**
  - No documentation found.

- **test_other_command_invoke_with_defaults**
  - No documentation found.

- **cli**
  - No documentation found.

- **other_cmd**
  - No documentation found.

- **test_invoked_subcommand**
  - No documentation found.

- **cli**
  - No documentation found.

- **sync**
  - No documentation found.

- **test_aliased_command_canonical_name**
  - No documentation found.

- **AliasedGroup**
  - No documentation found.

- **get_command**
  - No documentation found.

- **resolve_command**
  - No documentation found.

- **push**
  - No documentation found.

- **test_group_add_command_name**
  - No documentation found.

- **test_iter_params_for_processing**
  - No documentation found.

- **test_help_param_priority**
  - Cover the edge-case in which the eagerness of help option was not
    respected, because it was internally generated multiple times.

    See: https://github.com/pallets/click/pull/2811

- **print_and_exit**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_unprocessed_options**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_in_help_messages**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_in_invocation**
  - No documentation found.

- **deprecated_cmd**
  - No documentation found.

- **test_command_parse_args_collects_option_prefixes**
  - No documentation found.

- **test**
  - No documentation found.

- **test_group_parse_args_collects_base_option_prefixes**
  - No documentation found.

- **group**
  - No documentation found.

- **command1**
  - No documentation found.

- **command2**
  - No documentation found.

- **test_group_invoke_collects_used_option_prefixes**
  - No documentation found.

- **group**
  - No documentation found.

- **command1**
  - No documentation found.

- **command2**
  - No documentation found.

- **test_abort_exceptions_with_disabled_standalone_mode**
  - No documentation found.

- **cli**
  - No documentation found.


### tests\test_command_decorators.py

- **test_command_no_parens**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_custom_command_no_parens**
  - No documentation found.

- **CustomCommand**
  - No documentation found.

- **CustomGroup**
  - No documentation found.

- **grp**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_group_no_parens**
  - No documentation found.

- **grp**
  - No documentation found.

- **cmd1**
  - No documentation found.

- **grp2**
  - No documentation found.

- **cmd2**
  - No documentation found.

- **test_params_argument**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_generate_name**
  - No documentation found.

- **f**
  - No documentation found.


### tests\test_compat.py

- **test_is_jupyter_kernel_output**
  - No documentation found.

- **JupyterKernelFakeStream**
  - No documentation found.


### tests\test_context.py

- **test_ensure_context_objects**
  - No documentation found.

- **Foo**
  - No documentation found.

- **__init__**
  - No documentation found.

- **cli**
  - No documentation found.

- **test**
  - No documentation found.

- **test_get_context_objects**
  - No documentation found.

- **Foo**
  - No documentation found.

- **__init__**
  - No documentation found.

- **cli**
  - No documentation found.

- **test**
  - No documentation found.

- **test_get_context_objects_no_ensuring**
  - No documentation found.

- **Foo**
  - No documentation found.

- **__init__**
  - No documentation found.

- **cli**
  - No documentation found.

- **test**
  - No documentation found.

- **test_get_context_objects_missing**
  - No documentation found.

- **Foo**
  - No documentation found.

- **cli**
  - No documentation found.

- **test**
  - No documentation found.

- **test_multi_enter**
  - No documentation found.

- **cli**
  - No documentation found.

- **callback**
  - No documentation found.

- **test_global_context_object**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_context_meta**
  - No documentation found.

- **set_language**
  - No documentation found.

- **get_language**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_make_pass_meta_decorator**
  - No documentation found.

- **cli**
  - No documentation found.

- **show**
  - No documentation found.

- **test_make_pass_meta_decorator_doc**
  - No documentation found.

- **test_context_pushing**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_callback**
  - No documentation found.

- **test_pass_obj**
  - No documentation found.

- **cli**
  - No documentation found.

- **test**
  - No documentation found.

- **test_close_before_pop**
  - No documentation found.

- **cli**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_close_before_exit**
  - No documentation found.

- **cli**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_multiple_eager_callbacks**
  - Checks all callbacks are called on exit, even the nasty ones hidden within
    callbacks.

    Also checks the order in which they're called.

- **NonExitingOption**
  - No documentation found.

- **reset_state**
  - No documentation found.

- **set_state**
  - No documentation found.

- **__init__**
  - No documentation found.

- **ExitingOption**
  - No documentation found.

- **set_state**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_no_state_leaks**
  - Demonstrate state leaks with a specific case of the generic test above.

    Use a logger as a real-world example of a common fixture which, due to its global
    nature, can leak state if not clean-up properly in a callback.

- **DebugLoggerOption**
  - A custom option to set the name of the debug logger.

- **reset_loggers**
  - Forces logger managed by the option to be reset to the default level.

- **set_level**
  - No documentation found.

- **__init__**
  - No documentation found.

- **messing_with_logger**
  - No documentation found.

- **test_with_resource**
  - No documentation found.

- **manager**
  - No documentation found.

- **test_with_resource_exception**
  - No documentation found.

- **TestContext**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **TestException**
  - No documentation found.

- **test_with_resource_nested_exception**
  - No documentation found.

- **TestContext**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__enter__**
  - No documentation found.

- **__exit__**
  - No documentation found.

- **TestException**
  - No documentation found.

- **test_make_pass_decorator_args**
  - Test to check that make_pass_decorator doesn't consume arguments based on
    invocation order.

- **Foo**
  - No documentation found.

- **cli**
  - No documentation found.

- **test1**
  - No documentation found.

- **test2**
  - No documentation found.

- **test_propagate_show_default_setting**
  - A context's ``show_default`` setting defaults to the value from
    the parent context.

- **test_exit_not_standalone**
  - No documentation found.

- **cli**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_parameter_source**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_propagate_opt_prefixes**
  - No documentation found.


### tests\test_custom_classes.py

- **test_command_context_class**
  - A command with a custom ``context_class`` should produce a
    context using that type.

- **CustomContext**
  - No documentation found.

- **CustomCommand**
  - No documentation found.

- **test_context_invoke_type**
  - A command invoked from a custom context should have a new
    context with the same type.

- **CustomContext**
  - No documentation found.

- **CustomCommand**
  - No documentation found.

- **second**
  - No documentation found.

- **first**
  - No documentation found.

- **test_context_formatter_class**
  - A context with a custom ``formatter_class`` should format help
    using that type.

- **CustomFormatter**
  - No documentation found.

- **write_heading**
  - No documentation found.

- **CustomContext**
  - No documentation found.

- **test_group_command_class**
  - A group with a custom ``command_class`` should create subcommands
    of that type by default.

- **CustomCommand**
  - No documentation found.

- **CustomGroup**
  - No documentation found.

- **test_group_group_class**
  - A group with a custom ``group_class`` should create subgroups
    of that type by default.

- **CustomSubGroup**
  - No documentation found.

- **CustomGroup**
  - No documentation found.

- **test_group_group_class_self**
  - A group with ``group_class = type`` should create subgroups of
    the same type as itself.

- **CustomGroup**
  - No documentation found.


### tests\test_defaults.py

- **test_basic_defaults**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_multiple_defaults**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_nargs_plus_multiple**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_multiple_flag_default**
  - Default default for flags when multiple=True should be empty tuple.

- **cli**
  - No documentation found.

- **test_flag_default_map**
  - test flag with default map

- **cli**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_shared_param_prefers_first_default**
  - test that the first default is chosen when multiple flags share a param name

- **prefers_green**
  - No documentation found.

- **prefers_red**
  - No documentation found.


### tests\test_formatting.py

- **test_basic_functionality**
  - No documentation found.

- **cli**
  - First paragraph.

        This is a very long second
        paragraph and not correctly
        wrapped but it will be rewrapped.

        \b
        This is
        a paragraph
        without rewrapping.

        \b
        1
         2
          3

        And this is a paragraph
        that will be rewrapped again.

- **test_wrapping_long_options_strings**
  - No documentation found.

- **cli**
  - Top level command

- **a_very_long**
  - Second level

- **command**
  - A command.

- **test_wrapping_long_command_name**
  - No documentation found.

- **cli**
  - Top level command

- **a_very_very_very_long**
  - Second level

- **command**
  - A command.

- **test_formatting_empty_help_lines**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_formatting_usage_error**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_formatting_usage_error_metavar_missing_arg**
  - :author: @r-m-n
    Including attribution to #612

- **cmd**
  - No documentation found.

- **test_formatting_usage_error_metavar_bad_arg**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_formatting_usage_error_nested**
  - No documentation found.

- **cmd**
  - No documentation found.

- **foo**
  - No documentation found.

- **test_formatting_usage_error_no_help**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_formatting_usage_custom_help**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_formatting_custom_type_metavar**
  - No documentation found.

- **MyType**
  - No documentation found.

- **get_metavar**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_truncating_docstring**
  - No documentation found.

- **cli**
  - First paragraph.

        This is a very long second
        paragraph and not correctly
        wrapped but it will be rewrapped.
        \f

        :param click.core.Context ctx: Click context.

- **test_truncating_docstring_no_help**
  - No documentation found.

- **cli**
  - \f

        This text should be truncated.

- **test_removing_multiline_marker**
  - No documentation found.

- **cli**
  - No documentation found.

- **cmd1**
  - \b
        This is command with a multiline help text
        which should not be rewrapped.
        The output of the short help text should
        not contain the multiline marker.

- **test_global_show_default**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_formatting_with_options_metavar_empty**
  - No documentation found.

- **test_help_formatter_write_text**
  - No documentation found.


### tests\test_imports.py

- **tracking_import**
  - No documentation found.

- **test_light_imports**
  - No documentation found.


### tests\test_info_dict.py

- **test_parameter**
  - No documentation found.

- **test_command**
  - No documentation found.

- **test_context**
  - No documentation found.

- **test_paramtype_no_name**
  - No documentation found.

- **TestType**
  - No documentation found.


### tests\test_normalization.py

- **test_option_normalization**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choice_normalization**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_command_normalization**
  - No documentation found.

- **cli**
  - No documentation found.

- **foo**
  - No documentation found.


### tests\test_options.py

- **test_prefixes**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_invalid_option**
  - No documentation found.

- **test_deprecated_usage**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_deprecated_warning**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_deprecated_required**
  - No documentation found.

- **test_deprecated_prompt**
  - No documentation found.

- **test_invalid_nargs**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_nargs_tup_composite_mult**
  - No documentation found.

- **copy**
  - No documentation found.

- **test_counting**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_unknown_options**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_suggest_possible_options**
  - No documentation found.

- **test_multiple_required**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_good_defaults_for_multiple**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_bad_defaults_for_multiple**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_empty_envvar**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_multiple_envvar**
  - No documentation found.

- **cmd**
  - No documentation found.

- **cmd**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_boolean_flag_envvar**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_boolean_envvar_bad_values**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_multiple_default_help**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_show_default_default_map**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_multiple_default_type**
  - No documentation found.

- **test_multiple_default_composite_type**
  - No documentation found.

- **test_parse_multiple_default_composite_type**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_dynamic_default_help_unset**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_dynamic_default_help_text**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_dynamic_default_help_special_method**
  - No documentation found.

- **Value**
  - No documentation found.

- **__call__**
  - No documentation found.

- **__str__**
  - No documentation found.

- **test_intrange_default_help_text**
  - No documentation found.

- **test_count_default_type_help**
  - A count option with the default type should not show >=0 in help.

- **test_file_type_help_default**
  - The default for a File type is a filename string. The string
    should be displayed in help, not an open file object.

    Type casting is only applied to defaults in processing, not when
    getting the default value.

- **test_toupper_envvar_prefix**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_nargs_envvar**
  - No documentation found.

- **cmd**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_show_envvar**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_show_envvar_auto_prefix**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_show_envvar_auto_prefix_dash_in_command**
  - No documentation found.

- **cli**
  - No documentation found.

- **foo_bar**
  - No documentation found.

- **test_custom_validation**
  - No documentation found.

- **validate_pos_int**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_callback_validates_prompt**
  - No documentation found.

- **validate**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_winstyle_options**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_legacy_options**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_required_option**
  - No documentation found.

- **test_missing_required_flag**
  - No documentation found.

- **test_missing_choice**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_missing_envvar**
  - No documentation found.

- **test_case_insensitive_choice**
  - No documentation found.

- **cmd**
  - No documentation found.

- **cmd2**
  - No documentation found.

- **test_case_insensitive_choice_returned_exactly**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_option_help_preserve_paragraphs**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_argument_custom_class**
  - No documentation found.

- **CustomArgument**
  - No documentation found.

- **get_default**
  - a dumb override of a default value for testing

- **cmd**
  - No documentation found.

- **test_option_custom_class**
  - No documentation found.

- **CustomOption**
  - No documentation found.

- **get_help_record**
  - a dumb override of a help text for testing

- **cmd**
  - No documentation found.

- **test_option_custom_class_can_override_type_cast_value_and_never_sees_unset**
  - Test that overriding type_cast_value is supported

    In particular, the option is never passed an UNSET sentinel value.

- **CustomOption**
  - No documentation found.

- **type_cast_value**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_option_custom_class_reusable**
  - Ensure we can reuse a custom class option. See Issue #926

- **CustomOption**
  - No documentation found.

- **get_help_record**
  - a dumb override of a help text for testing

- **cmd1**
  - No documentation found.

- **cmd2**
  - No documentation found.

- **test_help_option_custom_names_and_class**
  - No documentation found.

- **CustomHelpOption**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_bool_flag_with_type**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_aliases_for_flags**
  - No documentation found.

- **cli**
  - No documentation found.

- **cli_alt**
  - No documentation found.

- **test_option_names**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_flag_duplicate_names**
  - No documentation found.

- **test_show_default_boolean_flag_name**
  - When a boolean flag has distinct True/False opts, it should show
    the default opt name instead of the default value. It should only
    show one name even if multiple are declared.

- **test_show_true_default_boolean_flag_value**
  - When a boolean flag only has one opt and its default is True,
    it will show the default value, not the opt name.

- **test_hide_false_default_boolean_flag_value**
  - When a boolean flag only has one opt and its default is False or
    None, it will not show the default

- **test_show_default_string**
  - When show_default is a string show that value as default.

- **test_show_default_with_empty_string**
  - When show_default is True and default is set to an empty string.

- **test_do_not_show_no_default**
  - When show_default is True and no default is set do not show None.

- **test_do_not_show_default_empty_multiple**
  - When show_default is True and multiple=True is set, it should not
    print empty default value in --help output.

- **test_show_default_precedence**
  - No documentation found.

- **test_option_with_optional_value**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_multiple_option_with_optional_value**
  - No documentation found.

- **test_type_from_flag_value**
  - No documentation found.

- **test_flag_value_and_default**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_invalid_flag_definition**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_default_dual_option_callback**
  - Check how default is processed by the callback when options compete for the same
    variable name.

    Reproduction of the issue reported in
    https://github.com/pallets/click/pull/3030#discussion_r2271571819

- **_my_func**
  - No documentation found.

- **main**
  - No documentation found.

- **test_envvar_string_flag_value**
  - Ensure that flag_value is recognized by the envvar.

- **cmd**
  - No documentation found.

- **test_flag_auto_detection**
  - No documentation found.

- **test_invalid_flag_combinations**
  - No documentation found.

- **test_non_flag_with_non_negatable_default**
  - No documentation found.

- **NonNegatable**
  - No documentation found.

- **__bool__**
  - No documentation found.

- **cmd**
  - No documentation found.

- **HashType**
  - No documentation found.

- **Number**
  - No documentation found.

- **Letter**
  - No documentation found.

- **Color**
  - No documentation found.

- **ColorInt**
  - No documentation found.

- **test_choice_usage_rendering**
  - BY default ``--help`` prints choice's values in the usage message.

    But ``show_choices=False`` makes ``--help`` prints choice's METAVAR instead of
    values.

    Also check that usage error message always suggests the actual values.

- **cli_with_choices**
  - No documentation found.

- **cli_without_choices**
  - No documentation found.

- **test_choice_default_rendering**
  - No documentation found.

- **cli_with_choices**
  - No documentation found.

- **test_duplicate_names_warning**
  - No documentation found.

- **cli**
  - No documentation found.

- **EnumSentinel**
  - No documentation found.

- **__bool__**
  - Force the sentinel to be falsy to make sure it is not caught by Click
        internal implementation.

        Falsy sentinels have been discussed in:
        https://github.com/pallets/click/pull/3030#pullrequestreview-3106604795
        https://github.com/pallets/click/pull/3030#pullrequestreview-3108471552

- **test_dual_options_custom_type_sentinel_flag_value**
  - Check that an object-based sentinel, used as a flag value, is returned as-is
    to a custom type that is shared by two options, competing for the same variable
    name.

    A reproduction of
    https://github.com/pallets/click/issues/3024#issuecomment-3146511356

- **ConfigParamType**
  - A custom type that accepts a file path or a sentinel value.

- **convert**
  - No documentation found.

- **main**
  - No documentation found.

- **EngineType**
  - No documentation found.

- **Class1**
  - No documentation found.

- **Class2**
  - No documentation found.

- **test_custom_type_flag_value_standalone_option**
  - Test how the type and flag_value influence the returned value.

    Cover cases reported in:
    https://github.com/pallets/click/issues/3024#issuecomment-3146480714
    https://github.com/pallets/click/issues/2012#issuecomment-892437060

- **scan**
  - No documentation found.

- **is**
  - No documentation found.

- **test_custom_type_flag_value_dual_options**
  - Test how flag values are processed with dual options competing for the same
    variable name.

    Reproduce issues reported in:
    https://github.com/pallets/click/issues/3024#issuecomment-3146508536
    https://github.com/pallets/click/issues/2012#issue-946471049
    https://github.com/pallets/click/issues/2012#issuecomment-892437060

- **cli**
  - No documentation found.

- **test_custom_type_frozenset_flag_value**
  - Check that frozenset is correctly handled as a type, a flag value and a default.

    Reproduces https://github.com/pallets/click/issues/2610

- **rcli**
  - No documentation found.


### tests\test_parser.py

- **test_split_arg_string**
  - No documentation found.

- **test_parser_default_prefixes**
  - No documentation found.

- **test_parser_collects_prefixes**
  - No documentation found.


### tests\test_shell_completion.py

- **from**
  - No documentation found.

- **_get_words**
  - No documentation found.

- **test_command**
  - No documentation found.

- **test_group**
  - No documentation found.

- **test_nested_group**
  - No documentation found.

- **test_group_command_same_option**
  - No documentation found.

- **test_chained**
  - No documentation found.

- **test_help_option**
  - No documentation found.

- **test_argument_order**
  - No documentation found.

- **test_argument_default**
  - No documentation found.

- **test_type_choice**
  - No documentation found.

- **test_choice_special_characters**
  - No documentation found.

- **test_choice_conflicting_prefix**
  - No documentation found.

- **test_option_count**
  - No documentation found.

- **test_option_optional**
  - No documentation found.

- **test_path_types**
  - No documentation found.

- **test_absolute_path**
  - No documentation found.

- **test_option_flag**
  - No documentation found.

- **test_flag_option_with_nargs_option**
  - No documentation found.

- **test_option_custom**
  - No documentation found.

- **custom**
  - No documentation found.

- **test_option_multiple**
  - No documentation found.

- **test_option_nargs**
  - No documentation found.

- **test_argument_nargs**
  - No documentation found.

- **test_double_dash**
  - No documentation found.

- **test_hidden**
  - No documentation found.

- **test_add_different_name**
  - No documentation found.

- **test_completion_item_data**
  - No documentation found.

- **_patch_for_completion**
  - No documentation found.

- **test_full_source**
  - No documentation found.

- **test_full_complete**
  - No documentation found.

- **test_zsh_full_complete_with_colons**
  - No documentation found.

- **test_context_settings**
  - No documentation found.

- **complete**
  - No documentation found.

- **test_choice_case_sensitive**
  - No documentation found.

- **_restore_available_shells**
  - No documentation found.

- **test_add_completion_class**
  - No documentation found.

- **MyshComplete**
  - No documentation found.

- **should**
  - No documentation found.

- **MyshComplete**
  - No documentation found.

- **should**
  - No documentation found.

- **class**
  - No documentation found.

- **test_files_closed**
  - No documentation found.

- **cli**
  - No documentation found.


### tests\test_termui.py

- **FakeClock**
  - No documentation found.

- **__init__**
  - No documentation found.

- **advance_time**
  - No documentation found.

- **time**
  - No documentation found.

- **_create_progress**
  - No documentation found.

- **test_progressbar_strip_regression**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progressbar_length_hint**
  - No documentation found.

- **Hinted**
  - No documentation found.

- **__init__**
  - No documentation found.

- **__length_hint__**
  - No documentation found.

- **__iter__**
  - No documentation found.

- **__next__**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progressbar_no_tty**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progressbar_hidden_manual**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progressbar_time_per_iteration**
  - No documentation found.

- **test_progressbar_eta**
  - No documentation found.

- **test_progressbar_format_eta**
  - No documentation found.

- **test_progressbar_format_pos**
  - No documentation found.

- **test_progressbar_format_bar**
  - No documentation found.

- **test_progressbar_format_progress_line**
  - No documentation found.

- **test_progressbar_format_progress_line_with_show_func**
  - No documentation found.

- **item_show_func**
  - No documentation found.

- **test_progressbar_init_exceptions**
  - No documentation found.

- **test_progressbar_iter_outside_with_exceptions**
  - No documentation found.

- **test_progressbar_is_iterator**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_choices_list_in_prompt**
  - No documentation found.

- **cli_with_choices**
  - No documentation found.

- **cli_without_choices**
  - No documentation found.

- **test_file_prompt_default_format**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_secho**
  - No documentation found.

- **test_secho_non_text**
  - No documentation found.

- **test_progressbar_yields_all_items**
  - No documentation found.

- **test_progressbar_update**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progressbar_item_show_func**
  - item_show_func should show the current item being yielded.

- **cli**
  - No documentation found.

- **test_progressbar_update_with_item_show_func**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_progress_bar_update_min_steps**
  - No documentation found.

- **test_getchar_windows**
  - No documentation found.

- **test_getchar_special_key_windows**
  - No documentation found.

- **test_getchar_windows_exceptions**
  - No documentation found.

- **test_fast_edit**
  - No documentation found.

- **test_edit**
  - No documentation found.

- **test_prompt_required_with_required**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_prompt_required_false**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_confirmation_prompt**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_false_show_default_cause_no_default_display_in_prompt**
  - No documentation found.

- **cmd**
  - No documentation found.

- **test_flag_value_prompt**
  - Check how flag value are prompted and handled by all combinations of
    ``prompt``, ``default``, and ``flag_value`` parameters.

    Covers concerns raised in issue https://github.com/pallets/click/issues/1992.

- **cli**
  - No documentation found.


### tests\test_testing.py

- **test_runner**
  - No documentation found.

- **test**
  - No documentation found.

- **test_echo_stdin_stream**
  - No documentation found.

- **test**
  - No documentation found.

- **test_echo_stdin_prompts**
  - No documentation found.

- **test_python_input**
  - No documentation found.

- **test_prompt**
  - No documentation found.

- **test_hidden_prompt**
  - No documentation found.

- **test_multiple_prompts**
  - No documentation found.

- **test_runner_with_stream**
  - No documentation found.

- **test**
  - No documentation found.

- **test_prompts**
  - No documentation found.

- **test**
  - No documentation found.

- **test**
  - No documentation found.

- **test_getchar**
  - No documentation found.

- **continue_it**
  - No documentation found.

- **getchar_echo**
  - No documentation found.

- **test_catch_exceptions**
  - No documentation found.

- **CustomError**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_catch_exceptions_cli_runner**
  - Test that invoke `catch_exceptions` takes the value from CliRunner if not set
    explicitly.

- **CustomError**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_with_color**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_with_color_errors**
  - No documentation found.

- **CLIError**
  - No documentation found.

- **format_message**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_with_color_but_pause_not_blocking**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_exit_code_and_output_from_sys_exit**
  - No documentation found.

- **cli_string**
  - No documentation found.

- **cli_string_ctx_exit**
  - No documentation found.

- **cli_int**
  - No documentation found.

- **cli_int_ctx_exit**
  - No documentation found.

- **cli_float**
  - No documentation found.

- **cli_float_ctx_exit**
  - No documentation found.

- **cli_no_error**
  - No documentation found.

- **test_env**
  - No documentation found.

- **cli_env**
  - No documentation found.

- **test_stderr**
  - No documentation found.

- **cli_stderr**
  - No documentation found.

- **cli_empty_stderr**
  - No documentation found.

- **test_args**
  - No documentation found.

- **cli_args**
  - No documentation found.

- **test_setting_prog_name_in_extra**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_command_standalone_mode_returns_value**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_file_stdin_attrs**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_isolated_runner**
  - No documentation found.

- **test_isolated_runner_custom_tempdir**
  - No documentation found.

- **test_isolation_stderr_errors**
  - Writing to stderr should escape invalid characters instead of
    raising a UnicodeEncodeError.

- **test_isolation_flushes_unflushed_stderr**
  - An un-flushed write to stderr, as with `print(..., file=sys.stderr)`, will end up
    flushed by the runner at end of invocation.

- **cli**
  - No documentation found.


### tests\test_types.py

- **test_range**
  - No documentation found.

- **test_range_fail**
  - No documentation found.

- **test_float_range_no_clamp_open**
  - No documentation found.

- **test_cast_multi_default**
  - No documentation found.

- **test_path_type**
  - No documentation found.

- **_symlinks_supported**
  - No documentation found.

- **test_path_resolve_symlink**
  - No documentation found.

- **_non_utf8_filenames_supported**
  - No documentation found.

- **test_path_surrogates**
  - No documentation found.

- **no_access**
  - Test environments may be running as root, so we have to fake the result of
        the access tests that use os.access

- **test_file_surrogates**
  - No documentation found.

- **test_file_error_surrogates**
  - No documentation found.

- **test_invalid_path_with_esc_sequence**
  - No documentation found.

- **test_choice_get_invalid_choice_message**
  - No documentation found.


### tests\test_utils.py

- **test_unset_sentinel**
  - No documentation found.

- **test_echo**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_echo_custom_file**
  - No documentation found.

- **test_echo_no_streams**
  - echo should not fail when stdout and stderr are None with pythonw on Windows.

- **test_styling**
  - No documentation found.

- **test_unstyle_other_ansi**
  - No documentation found.

- **test_filename_formatting**
  - No documentation found.

- **test_prompts**
  - No documentation found.

- **test**
  - No documentation found.

- **test_no**
  - No documentation found.

- **test_confirm_repeat**
  - No documentation found.

- **test_prompts_abort**
  - No documentation found.

- **f**
  - No documentation found.

- **test_prompts_eof**
  - If too few lines of input are given, prompt should exit, not hang.

- **echo**
  - No documentation found.

- **_test_gen_func**
  - No documentation found.

- **_test_gen_func_fails**
  - No documentation found.

- **_test_gen_func_echo**
  - No documentation found.

- **_test_simulate_keyboard_interrupt**
  - No documentation found.

- **test_echo_via_pager**
  - No documentation found.

- **test_echo_color_flag**
  - No documentation found.

- **test_prompt_cast_default**
  - No documentation found.

- **test_echo_writing_to_standard_error**
  - No documentation found.

- **emulate_input**
  - Emulate keyboard input.

- **test_echo_with_capsys**
  - No documentation found.

- **test_open_file**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_open_file_pathlib_dash**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_open_file_ignore_errors_stdin**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_open_file_respects_ignore**
  - No documentation found.

- **test_open_file_ignore_invalid_utf8**
  - No documentation found.

- **test_open_file_ignore_no_encoding**
  - No documentation found.

- **test_open_file_atomic_permissions_existing_file**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_open_file_atomic_permissions_new_file**
  - No documentation found.

- **cli**
  - No documentation found.

- **test_iter_keepopenfile**
  - No documentation found.

- **test_iter_lazyfile**
  - No documentation found.

- **MockMain**
  - No documentation found.

- **__init__**
  - No documentation found.

- **test_detect_program_name**
  - No documentation found.

- **test_expand_args**
  - No documentation found.

- **test_make_default_short_help**
  - No documentation found.


### tests\typing\typing_aliased_group.py

- **AliasedGroup**
  - No documentation found.

- **get_command**
  - No documentation found.

- **resolve_command**
  - No documentation found.

- **cli**
  - No documentation found.

- **push**
  - No documentation found.

- **pop**
  - No documentation found.


### tests\typing\typing_confirmation_option.py

- **dropdb**
  - No documentation found.


### tests\typing\typing_group_kw_options.py

- **hello**
  - No documentation found.


### tests\typing\typing_help_option.py

- **hello**
  - Simple program that greets NAME for a total of COUNT times.


### tests\typing\typing_options.py

- **hello**
  - No documentation found.


### tests\typing\typing_password_option.py

- **encrypt**
  - No documentation found.


### tests\typing\typing_progressbar.py

- **test_length_is_int**
  - No documentation found.

- **it**
  - No documentation found.

- **test_generic_on_iterable**
  - No documentation found.


### tests\typing\typing_simple_example.py

- **hello**
  - No documentation found.


### tests\typing\typing_version_option.py

- **hello**
  - No documentation found.


    