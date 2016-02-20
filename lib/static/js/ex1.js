
function search(){
  console.log("search");
  $.ajax({
    url: '/hello/search',
    data: {
      city:document.getElementById('city').value,
      date:document.getElementById('datepicker').value,
      role:document.getElementById('role').value
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

function post_request(){

  console.log("hi");


  $.ajax({
    url: '/hello/post_request',
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

function post_offer(){

  console.log("hi");


  $.ajax({
    url: '/hello/post_offer',
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