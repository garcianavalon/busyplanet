var map = function() {
    var text = String(this.text);
    if (text) {
        // quick lowercase to normalize per your requirements
        text = text.toLowerCase().split(" ");
        for (var i = text.length - 1; i >= 0; i--) {
            // might want to remove punctuation, etc. here
            if (text[i])  {      // make sure there's something
               emit(text[i], 1); // store a 1 for each word
            }
        }
    }
};