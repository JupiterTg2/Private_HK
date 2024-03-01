#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'm{CMD_SUFFIX}', f'mirror{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qm{CMD_SUFFIX}', f'qbmirror{CMD_SUFFIX}']
        self.YtdlCommand = [f'xxyt{CMD_SUFFIX}', f'xxytdl{CMD_SUFFIX}']
        self.LeechCommand = [f'l{CMD_SUFFIX}', f'leech{CMD_SUFFIX}']
        self.QbLeechCommand = [f'ql{CMD_SUFFIX}', f'qbleech{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'xxytl{CMD_SUFFIX}', f'xxytdlleech{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'uzm{CMD_SUFFIX}', f'unzipmirror{CMD_SUFFIX}', f'zm{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbuzm{CMD_SUFFIX}', f'qbunzipmirror{CMD_SUFFIX}', f'qbzm{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'xxytz{CMD_SUFFIX}', f'xxytdlzip{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'uzl{CMD_SUFFIX}', f'unzipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbuzl{CMD_SUFFIX}', f'qbunzipleech{CMD_SUFFIX}', f'qbzl{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'xxytzl{CMD_SUFFIX}', f'xxytdlzipleech{CMD_SUFFIX}'])
        self.CloneCommand = [f'c{CMD_SUFFIX}', f'clone{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = f'can{CMD_SUFFIX}'
        self.CancelAllCommand = [f'canall{CMD_SUFFIX}', 'canall']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f's{CMD_SUFFIX}', f'status{CMD_SUFFIX}', 'sall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'auth{CMD_SUFFIX}', f'authorize{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauth{CMD_SUFFIX}', f'unauthorize{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'xping{CMD_SUFFIX}', f'xp{CMD_SUFFIX}']
        self.RestartCommand = [f'r{CMD_SUFFIX}', f'restart{CMD_SUFFIX}', 'rtall']
        self.StatsCommand = [f'xst{CMD_SUFFIX}', f'xstats{CMD_SUFFIX}']
        self.HelpCommand = f'xhelp{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = [f'cl{CMD_SUFFIX}', f'clearlocals{CMD_SUFFIX}']
        self.BotSetCommand = [f'bs{CMD_SUFFIX}', f'bsetting{CMD_SUFFIX}']
        self.UserSetCommand = [f'us{CMD_SUFFIX}', f'usetting{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'xsp{CMD_SUFFIX}', f'xspeedtest{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mi{CMD_SUFFIX}', f'mediainfo{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gc{CMD_SUFFIX}', f'gdclean{CMD_SUFFIX}']
        self.BroadcastCommand = [f'bc{CMD_SUFFIX}', f'broadcast{CMD_SUFFIX}']

BotCommands = _BotCommands()
