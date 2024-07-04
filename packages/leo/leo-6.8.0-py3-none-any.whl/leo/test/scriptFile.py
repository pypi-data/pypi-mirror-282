#@+leo-ver=5-thin
#@+node:ekr.20111006212449.11850: * @button check-settings
'''Check the consistency of all settings.'''
# https://github.com/leo-editor/leo-editor/issues/993
# https://github.com/leo-editor/leo-editor/issues/1511

class Controller:
    #@+others
    #@+node:ekr.20111006212449.11851: ** ctor
    def __init__(self, c):
        self.c = c
        self.errors = 0
        # Commanders...
        self.core = None  # leoPy.leo.
        self.settings = None  # leoSettings.leo.
        self.user_settings = None  # myLeoSettings.leo
    #@+node:ekr.20111006212449.11852: ** check & helpers
    def check(self, configs_d, settings_d):
        munge = self.munge
        table = ('Bool', 'Int', 'Float', 'Ratio', 'Path', 'String',) # 'Color', 'Font',
        
        def printList(aList):
            if len(aList) < 2:
                print('  ', aList[0])
            else:
                g.printObj(aList)
        #
        # Print missing user settings...
        for kind in table:
            config_key = 'get%s' % kind
            settings_key = '@%s' % kind.lower()
            configs = configs_d.get(config_key, [])
            settings = settings_d.get(settings_key, [])
            m_configs = [munge(z) for z in configs]
            m_settings = [munge(z) for z in settings]
            missing = set([z for z in m_configs if not z in m_settings])
            aList = [z for z in missing if self.filter_user_config(z)]
            if aList:
                print('\nmissing %s %s settings...\n' % (len(aList), settings_key))
                for z in sorted(aList):
                    aList2 = [z2 for z2 in configs if munge(z2) == munge(z)]
                    printList(aList2)
        #
        # Print missing calls to c.config.getX...
        for kind in table:
            config_key = 'get%s' % kind
            settings_key = '@%s' % kind.lower()
            configs = configs_d.get(config_key, [])
            settings = settings_d.get(settings_key, [])
            m_configs = [munge(z) for z in configs]
            m_settings = [munge(z) for z in settings]
            missing = set([z for z in m_settings if not z in m_configs])
            aList = [z for z in missing if self.filter_get_x(z)]
            if aList:
                print(f"missing {len(aList)} config.{config_key} calls:")
                for z in sorted(aList):
                    aList2 = [z2 for z2 in settings if munge(z2) == munge(z)]
                    printList(aList2)
    #@+node:ekr.20181018060340.1: *3* filter_get_x
    def filter_get_x(self, setting):
        '''
        Return False if we can safely ignore a missing call to config.get(setting).
        
        Everything here is a hack. Some are bigger than others.
        '''
        munge = self.munge
        #
        # These *ivars* are set by the GlobalConfigManager class.
        # There *should* be settings for all of these, despite missing config.get calls.
        table = (
            # encodingIvarsDict...
                "default_at_auto_file_encoding",
                "default_derived_file_encoding",
                "new_leo_file_encoding",
            # defaultsDict...
                "color_directives_in_plain_text",
                "output_doc_chunks",
                "page_width",
                "tab_width",
                "tangle_outputs_header",
                "target_language",
                "underline_undefined_section_names",
            # ivarsDict
                "at_root_bodies_start_in_doc_mode",
                "create_nonexistent_directories",
                "output_initial_comment",
                "output_newline",
                "page_width",
                "read_only",
                "redirect_execute_script_output_to_log_pane",
                "relative_path_base_directory",
                "remove_sentinels_extension",
                "save_clears_undo_buffer",
                "stylesheet",
                "tab_width",
                "target_language",
                "trailing_body_newlines",
                "use_plugins",
                "undo_granularity",
                "write_strips_blank_lines",
        )
        table = [munge(z) for z in table]
        if setting in table:
            return False
        #
        # unitTest.leo tests test-darwin-setting and test-win32-setting
        if setting in ('testdarwinsetting', 'testwin32setting'):
            return False
        #
        # Stylesheets use these settings.
        for pattern in (
            'bg', 'border', 'color', 'fg', 'font',
            'leogreen', 'leoyello',
            'margin', 'padding', 'relief',
            'solarized', 'split-bar', 'text-foreground', 'tree-image',
        ):
            if setting.find(munge(pattern)) > -1:
                return False
        #
        # These plugins/use settings in non-standard ways.
        if setting.startswith((
                'bookmarks', 'datenodes', 'http', 'opml',
                'rst3', 'todo', 'vim', 'zodb'
            ),
        ):
            return False
        #
        # Find settings are defined in non-standard ways.
        for pattern in (
            'batch', 'change-text',
            'find-def-creates-clones',
            'find-text', 'ignore-case',
            'mark-changes', 'mark-finds', 'node-only', 'pattern-match',
            'reverse', 'search-body', 'search-headline', 'suboutline-only',
            'whole-word', 'wrap',
        ):
            if setting == munge(pattern):
                return False
        #
        # Issue a warning.
        return True
    #@+node:ekr.20181018065113.1: *3* filter_user_config
    def filter_user_config(self, setting):
        '''
        Return False if we can safely ignore a setting that does not exist in leoSettings.leo.
        
        Everything here is a hack. Some are bigger than others.
        '''
        munge = self.munge
        #
        # unitTest.leo tests test-darwin-setting and test-win32-setting
        if setting in ('testdarwinsetting', 'testwin32setting'):
            return False
        #
        # The calls to config.get* are commented out in the code,
        # but get_configs isn't smart enough to know that.
        for ignore in (
            'theme-name',
            'pytest-path', # In a (disabled) @button node
            'leo-to-html-%s', # Loads multiple settings from an .ini file.
        ):
            if setting == munge(ignore):
                return False
        #
        # Stylesheets use these settings.
        # It would be a major project to discover what settings
        # are actually used in the present stylesheet.
        for pattern in (
            'bg', 'border', 'color', 'fg', 'font',
            'leogreen', 'leoyello',
            'margin', 'padding', 'relief',
            'solarized', 'split-bar', 'text-foreground', 'tree-image',
        ):
            if munge(pattern) in setting:
                return False
        #
        # These plugins use settings in non-standard ways.
        if setting.startswith((
            'activepath', 'bookmarks', 'datenodes', 'http', 'opml',
            'rst3', 'todo', 'vim', 'vr3', 'zodb'),
        ):
            return False
        #
        # Find settings are defined in non-standard ways.
        for pattern in (
            'batch', 'change-text', 'find-text', 'ignore-case',
            'mark-changes', 'mark-finds', 'node-only', 'pattern-match',
            'reverse', 'search-body', 'search-headline', 'suboutline-only',
            'whole-word', 'wrap',
        ):
            if setting == munge(pattern):
                return False
        #
        # Tangle/untagle settings are deprecated and imo should not exist.
        for pattern in (
            'output-doc-flag', 'tangle-batch-flag',
            'untangle-batch-flag', 'use-header-flag',
        ):
            if setting == munge(pattern):
                return False
        #
        # Issue a warning.
        return True
    #@+node:ekr.20200226105416.1: ** check_user_settings
    def check_user_settings(self, settings_d, user_settings_d):
        """
        Report settings in myLeoSettings.leo that are not in leoSettings.leo.
        
        This method requires exact matches between settings: it does no munging.
        """
        unusual_keys = (
            '@color',  # per-key @color settings have changed.
        )
        unusual_settings = (
            # 'forth',  # Experimental.
            'color-theme',  # Uses td.get_string_setting.
            'theme-name',  # Uses td.get_string_setting.
        )
        for key in user_settings_d:
            settings = settings_d.get(key, [])
            user_settings = user_settings_d.get(key, [])
            for user_setting in user_settings:
                if (
                    user_setting not in settings
                    and user_setting not in unusual_settings
                    and key not in unusual_keys
                ):
                    print(f"Unknown setting in myLeoSettings.leo: {key} {user_setting}")
    #@+node:ekr.20111006212449.11853: ** error
    def error(self, s):
        print(s)
        self.errors += 1
    #@+node:ekr.20111006212449.11854: ** get_commanders
    def get_commanders(self):
        '''Open files as needed and set the commander ivars.'''

        def open_commander(fn):
            c = g.openWithFileName(fn, old_c=self.c, gui=g.app.nullGui)
            if not c:
                self.error('not found: %s' % fn)
            return c

        join, loadDir = g.os_path_join, g.app.loadDir
        self.core = open_commander(join(loadDir, '..', 'core', 'leoPy.leo'))
            # Opening LeoPyRef.leo would be slower.
        self.settings = open_commander(join(loadDir, '..', 'config', 'leoSettings.leo'))
        self.user_settings = open_commander(g.app.loadManager.my_settings_path)
    #@+node:ekr.20111006212449.11855: ** get_configs & helpers
    def get_configs(self):
        '''
        Return a dict containing a representation of all calls to x.config.getX.
        '''
        d = {}
        for c in (self.core, ):
            print('scanning: %s' % c.shortFileName())
            self.get_configs_from_outline(c, d)
        return d
    #@+node:ekr.20111006212449.11856: *3* get_configs_from_outline & helper
    def get_configs_from_outline(self, c, d):
        '''
        Scan the outline for all calls to x.config.getX and add items to d.
        '''
        p = c.rootPosition()
        while p:
            if '@nosearch' in p.b:  # #1511.
                # print('ignore', p.h)
                p.moveToNodeAfterTree()
            else:
                self.scan_for_configs(p, d)
                p.moveToThreadNext()
        return d
    #@+node:ekr.20111006212449.11857: *4* scan_for_configs
    def scan_for_configs(self, p, d):
        '''
        Scan the body text of p, finding all calls to config.getX.
        
        This code does not know about `if 0`, but does know about comments.
        '''
        kinds = (
            'getBool', 'getColor', 'getInt', 'getFloat',
            'getPath', 'getRatio', 'getString',
            # '@font', # special case.
        )
        i, s = 0, p.b
        while i < len(s):
            progress = i
            ch = s[i]
            if (
                ch == '@' and
                (g.match(s, i, '@ ') or g.match(s, i, '@\n')) and
                (i == 0 or s[i - 1] == '\n')
            ):
                # Skip the @doc part.
                i = s.find('\n@c', i)
                if i == -1: break
            elif ch == '#':
                i = g.skip_to_end_of_line(s, i)
            elif ch in ('"', "'"):
                i = g.skip_python_string(s, i)
            elif ch == '_' or ch.isalpha():
                j = g.skip_id(s, i)
                kind = s[i: j]
                if kind in kinds:
                    # We have found a call to getBool, etc.
                    i = g.skip_ws(s, j)
                    if g.match(s, i, '('):
                        i = g.skip_ws_and_nl(s, i + 1)  # #1511.
                        if g.match(s, i, '"') or g.match(s, i, "'"):
                            j = g.skip_string(s, i)
                            name = s[i + 1: j - 1]
                            # print(f"{kind:12} {name}")
                            aList = d.get(kind, [])
                            if name not in aList:
                                aList.append(name)
                            d[kind] = aList
                    else:
                        j = i
                i = j
            else:
                i += 1
            assert progress < i
        return d
    #@+node:ekr.20111006212449.11858: ** get_settings & helper
    def get_settings(self, user):
        '''Return a dict containing a representation
        of all settings in leoSettings.leo or myLeoSettings.leo.
        '''
        trace = False
        c = self.user_settings if user else self.settings  # #1511.
        d = {}
        print('scanning: %s' % c.shortFileName())
        # #1792: Allow comments after @settings.
        settings_node = g.findNodeAnywhere(c, '@settings', exact=False)
        if not settings_node:
            return self.error('no @settings node')
        for p in settings_node.subtree():
            if self.is_setting(p):
                kind, name = self.parse_setting(p)
                if name:
                    # name = self.munge(name)
                    aList = d.get(kind, [])
                    if name not in aList:
                        aList.append(name)
                    d[kind] = aList
                else:
                    self.error('no name for %s' % (kind))
        if trace:
            keys = list(d.keys())
            for key in sorted(keys):
                print(key)
                aList = d.get(key)
                for name in sorted(aList):
                    print('  ' + name)
        return d
    #@+node:ekr.20111006212449.11859: *3* is_setting
    def is_setting(self, p):
        # For now, these are enough
        table = (
            '@bool', '@color', '@int', '@float',
            # '@font', # special case.
            '@ratio', '@path', '@string',
        )
        for s in table:
            if g.match_word(p.h, 0, s):
                return True
        return False
    #@+node:ekr.20111006212449.11860: *3* parse_setting
    def parse_setting(self, p):
        s = p.h
        assert s[0] == '@'
        i = g.skip_id(s, 1)
        kind = s[: i]
        assert kind
        i = g.skip_ws(s, i)
        j = g.skip_id(s, i, chars='-')
        name = s[i: j]
        return kind, name
    #@+node:ekr.20111006212449.11861: ** munge
    def munge(self, s):
        '''Return the canonicalized name for settings and arguments to c.config.getX.'''
        return g.toUnicode(s.replace('-', '').replace('_', '').lower())
    #@+node:ekr.20111006212449.11862: ** run
    def run(self):
        self.get_commanders()
        configs = self.get_configs()
        settings = self.get_settings(user=False)
        user_settings = self.get_settings(user=True)
        if self.errors == 0:
            self.check(configs, settings)
            self.check_user_settings(settings, user_settings)
        # Select leoSettings.leo.
        g.app.gui.frameFactory.setTabForCommander(self.settings)
        g.trace('done')
    #@-others

g.cls()
Controller(c).run()
#@-leo

