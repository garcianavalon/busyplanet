var mapFunction = function() {
    var text = this.text;
    if (text) {
        // quick lowercase to normalize per your requirements
        var aggregated_text = "";
        var string;
        for (string in text) {
            aggregated_text += string;
        }
        aggregated_text = aggregated_text.toLowerCase().split(" ");
        for (var i = aggregated_text.length - 1; i >= 0; i--) {
            // might want to remove punctuation, etc. here
            if (aggregated_text[i])  {      // make sure there's something
               emit(aggregated_text[i], 1); // store a 1 for each word
            }
        }
    }
};
var reduceFunction = function(key, values) {
    var count = 0;
    values.forEach(function(v) {
        count +=v;
    });
    return count;
};
db.runCommand(
               {
                 mapReduce: 'tripadvisor',
                 map: mapFunction,
                 reduce: reduceFunction,
                 out: { merge: 'map_reduce_results', db: 'bigdata' }
               }
             )