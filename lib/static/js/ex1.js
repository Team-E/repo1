
function ex1(){
  console.log("hi");
  $.ajax({
    url: '/hello/init',
    data: {
      query:document.getElementById('query').value
    },
    type: 'POST',
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function init1(){
  console.log("init");
  $.ajax({
    url: '/hello/hoge',
    data: {},
    type: 'POST',
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}