from enum import Enum


class Types(Enum):
    """Enum of supports types"""
    BACK_END = "Back-end"
    FRONT_END = "Front-end"
    ANDROID = "Android"
    IOS = "iOS"


class Tags(Enum):
    """Enum of tag types"""
    BUG = "Bug"
    TASK = "Task"
    IMPROVEMENT = "Improvement"


class Status(Enum):
    """Enum of status types"""
    TO_DO = "To do"
    IN_PROGRESS = "In progress"
    DONE = "Done"


class Priorities(Enum):
    """Enum of priorities types"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class ProjectRole(Enum):
    """Enum of role in a project"""
    AUTHOR = "Author"
    MANAGER = "Manager"
    CREATOR = "Creator"


class ProjectPermission(Enum):
    """Enum of project permissions"""
    READ = "Read"
    ALL = "All"
