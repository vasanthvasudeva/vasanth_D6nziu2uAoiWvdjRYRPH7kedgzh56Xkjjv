class Batsman:
    def __init__(self):
        self.strike_rate = 0.0
        self.total_runs = 0
        self.highest_score = 0
        self.batting_rank = 0
    def get_bat(self,sr,tr,hs,br):
        self.strike_rate = sr
        self.total_runs = tr
        self.highest_score = hs
        self.batting_rank = br
    def disp_bat(self):
        print "Strike Rate:",self.strike_rate
        print "Total Runs:",self.total_runs
        print "Highest Score:",self.highest_score
        print "Batting Rank:",self.batting_rank