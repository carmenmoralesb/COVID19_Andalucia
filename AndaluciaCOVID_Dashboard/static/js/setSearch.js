function setColorText() {
    if (window.matchMedia) {
      if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
        return "white";
      } else {
        return "black";
      }
    }
  } 