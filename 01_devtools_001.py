from textual import log

def on_mount(self) -> None:
    log("Hello, World") # simple string
    log(locals()) # log local variables
    log(children=self.children, pi=3.141592) # key/values
    log(self.tree) # Rich renderables