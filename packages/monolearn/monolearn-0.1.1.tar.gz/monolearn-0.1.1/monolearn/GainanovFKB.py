import logging

from monolearn.SparseSet import SparseSet

from .utils import truncstr, TimeStat
from .LearnModule import LearnModule


class GainanovFKB(LearnModule):
    log = logging.getLogger(f"{__name__}")

    def __init__(
        self,
        sense: str = None,  # min/max/None
        save_rate: int = 100,
        limit: int = None,
        start_level=None,
    ):
        assert sense in ("min", "max", None)
        self.do_min = sense == "min"
        self.do_max = sense == "max"
        self.do_opt = sense in ("min", "max")
        self.save_rate = int(save_rate)
        self.limit = None if limit is None else int(limit)
        self.start_level = start_level

    def _learn(self):
        self.

        self.level = None
        if self.do_opt:
            # check if not exhausted
            if not self.find_new_unknown():
                self.log.info("already exhausted, exiting")
                # if was not marked, we won't be here
                # so mark
                self.system.set_complete()
                return True

            if self.start_level is not None:
                self.level = self.start_level
            elif self.do_min:
                self.level = 0
            elif self.do_max:
                self.level = self.N
            else:
                assert 0
            assert 0 <= self.level <= self.N

            self.log.info(f"starting at level {self.level}")

        self.itr = 0
        while self.limit is None or self.itr < self.limit:
            if self.itr and self.itr % self.save_rate == 0:
                self.system.save()
            self.itr += 1

            unk = self.find_new_unknown()
            if unk is False:
                self.log.info("system is completed, saving")
                self.system.set_complete()
                return True

            self.learn_unknown(unk)
        self.system.save()
        return False

    @TimeStat.log
    def find_new_unknown(self):
        F = list(self.system.iter_lower())
        G = list(self.system.iter_upper())
        while True:
            nF = self.system.n_lower()
            nG = self.system.n_upper()
            if max(nF, nG) <= 1:
                # TODO
                return

    @TimeStat.log
    def learn_unknown(self, vec):
        is_lower, meta = self.query(vec)

        if is_lower:
            self.n_lower += 1
            if self.do_max:
                self.log.debug(f"fast lower: wt {len(vec)} meta {meta}")
                self.system.add_lower(vec, meta)
                self.model_exclude_sub(vec)
            else:
                self.learn_up(vec, meta)
        else:
            self.n_upper += 1
            if self.do_min:
                self.log.debug(f"fast upper: wt {len(vec)} meta {meta}")
                self.system.add_upper(vec, meta)
                self.model_exclude_super(vec)
            else:
                self.learn_down(vec, meta)
