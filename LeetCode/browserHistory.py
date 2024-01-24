class BrowserHistory:

    def __init__(self, homepage: str):
        self.historyList = [homepage]
        self.currentIdx = 0

    def visit(self, url: str) -> None:
        self.historyList[:self.currentIdx+1] + [url]
        self.currentIdx += 1

    def back(self, steps: int) -> str:
        self.currentIdx = max(self.currentIdx - steps, 0)
        return self.historyList[self.currentIdx]

    def forward(self, steps: int) -> str:
        self.currentIdx = min(self.currentIdx + steps, len(self.historyList) - 1)
        return self.historyList[self.currentIdx]



print([1]+[2])
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)