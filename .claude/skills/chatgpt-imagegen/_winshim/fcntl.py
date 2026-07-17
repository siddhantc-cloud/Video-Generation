"""Minimal Windows shim for the Unix-only `fcntl` module.

chatgpt-imagegen uses fcntl only for its cross-process concurrency slot pool
(advisory flock). Windows Python has no fcntl, so this shim provides no-op
locking: every slot acquires immediately. Safe for single/low-volume runs;
it does NOT enforce the concurrency cap across parallel processes.

Put this directory first on PYTHONPATH when invoking the CLI on Windows.
"""

LOCK_EX = 2
LOCK_SH = 1
LOCK_NB = 4
LOCK_UN = 8


def flock(fd, operation):  # no-op: advisory lock not enforced on Windows
    return None


def lockf(fd, operation, length=0, start=0, whence=0):  # no-op
    return None


def fcntl(fd, cmd, arg=0):  # no-op
    return 0


def ioctl(fd, request, arg=0, mutate_flag=True):  # no-op
    return 0
