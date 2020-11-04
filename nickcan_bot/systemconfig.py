from abc import ABC

import math
import os


HostUrl = os.environ.get("HOST_URL") or "http://localhost:8000"


class System:
    PingSpamWaitSeconds = 5 * 60  # 5 mins / Heroku sleep on 30 mins
    GitHubRepoIDName = "nick411077/nickcan_Bot"
    HerokuAppNameBeta = ""
    HerokuAppNameStable = "nickcan-discord-bot"
    MaxOneTimeResponses = 5
    MaxSendContentLength = 2000
    MaxSendContentLines = 20


class PlatformConfig(ABC):
    max_responses: int = NotImplementedError
    max_content_length: int = NotImplementedError
    max_content_lines: int = NotImplementedError


class AutoReply:
    MaxResponses = 5
    MaxContentLength = System.MaxSendContentLength
    TagSplittor = "|"
    CaseInsensitive = True
    BypassMultilineCDThresholdSeconds = 20


class Database:
    StatisticsExpirySeconds = 15811200  # 183 Days
    ExecodeExpirySeconds = 86400  # 24 Hrs
    CacheExpirySeconds = 172800  # 2 Days
    ExtraContentExpirySeconds = 2073600  # 30 Days
    BulkWriteCount = 300

    class PopularityConfig:
        TimeDiffIntersectHr = 168
        TimeFunctionCoeff = 40

        AppearanceIntersect = 100
        AppearanceFunctionCoeff = 1.4
        AppearanceEquivalentWHr = 5

        TimeCoeffA = 2 * TimeDiffIntersectHr
        TimeCoeffB = -1 / TimeFunctionCoeff
        AppearanceCoeffA = 1 / math.pow(AppearanceIntersect, AppearanceFunctionCoeff - 1)

    class MessageStats:
        MaxContentCharacter = 500


class DataQuery:
    TagPopularitySearchCount = 10


class ChannelConfig:
    VotesToPromoteMod = 7
    VotesToPromoteAdmin = 20


class Email:
    EmailCacheExpirySeconds = 3600  # 60 mins
    DefaultSubject = "Email Notification from Jelly BOT"
    DefaultPrefix = "Jelly BOT - "


class ExecodeManager:
    ChannelRegisterExecodeCooldownSeconds = 60


