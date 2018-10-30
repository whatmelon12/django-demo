
//"{% url 'polls:detail' question.id %}"
var exportModel = function(id){
    var url = 'http://' + $("#" + id).val();
    window.open(url);
}