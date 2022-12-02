let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
    let productId = this.dataset.product
    let action = this.dataset.action
    console.log('productId: ', productId, 'action: ', action)
    updateUserOrder(productId, action)
    console.log('User: ', user)
//    if(user === 'AnonymousUser'){
//        console.log('Not authurizated user')
//    }else{
//        updateUserOrder(productId, action)
//    }
//    })
// }


function updateUserOrder(productId, action){
    console.log('User authrozited, sending data..')

    let url = '/update_item/';

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})

    })

    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}
    }
//updateBtns = document.getElementsByClassName("update-cart");
//
//for (var i = 0; i < updateBtns.length; i++) {
//  updateBtns[i].addEventListener("click", function () {
//    var productId = this.dataset.product;
//    var action = this.dataset.action;
//
//    if (user === "AnonymousUser") {
//      console.log("Not Logged in");
//    } else {
//      updateUserOrder(productId, action);
//    }
//  });
//}
//
//function updateUserOrder(productId, action) {
//  var url = "/update_item/";
//
//  $.ajax({
//    url: url,
//    data: {
//      productId: productId,
//      action: action,
//    },
//    dataType: "json",
//
//    success: function (data) {
//      if (data.is_taken) {
//        alert("A user with this username already exists.");
//      }
//    },
//  });
//  console.log("productId:", productId, "action:", action);
//  console.log("USER:", user);
//  console.log(" User is logged in , Sending data...");
//}