createTableRow = (name, price, id) => {
    return (
        `<tr> 
        <th scope="col">${id}</th>
        <th scope="col">${name}</th>
        <th scope="col">${price}</th>
        <th scope="col"><button class="btn btn-warning my-2 my-sm-0 mr-sm-2" type="button" value =${id} onclick= "removeProduct(this)">Remove</button></th>
    </tr>`
    )
}

$.ajax({
    url: "http://127.0.0.1:8000/myapp/",
    cache: false,
    success: (res) => {
        item_array = JSON.parse(res)
        item_array_required = item_array.slice(1)
        item_array_required.forEach(element => {
            $("#item_table_body").append(createTableRow(element.name, element.price, element.id))
        });

    }
})

searchProduct = () => {
    console.log('submit')
    $("#item_table_body").empty()
    search_query = $("#search_input").val()
    console.log(search_query)
    $.ajax({
        url: `http://127.0.0.1:8000/myapp/search/${search_query}`,
        cache: false,
        success: (res) => {
            item_array = JSON.parse(res)
            console.log(item_array)
            item_array.forEach(element => {
                $("#item_table_body").append(createTableRow(element.name, element.price, element.id))
            });
        }
    })
}

viewAll = () => {
    $("#item_table_body").empty()
    $.ajax({
        url: "http://127.0.0.1:8000/myapp/",
        cache: false,
        success: (res) => {
            item_array = JSON.parse(res)
            item_array_required = item_array.slice(1)
            item_array_required.forEach(element => {
                $("#item_table_body").append(createTableRow(element.name, element.price, element.id))
            });
        }
    });
}

removeProduct = (button) => {
    

    $.ajax({
        url: `http://127.0.0.1:8000/myapp/remove/${button.value}`,
        cache: false,
        success: (res) => {
            $("#item_table_body").empty()
            item_array = JSON.parse(res)
            // console.log(item_array)
            item_array_required = item_array.array.slice(1)
            item_array_required.forEach(element => {
                $("#item_table_body").append(createTableRow(element.name, element.price, element.id))
            });

        }
    });

};

addProduct = () => {
    var id = $("#productID").val()
    var name = $("#productName").val()
    var price = $("#productPrice").val()

    if (id == '' || name == '' || price == '') {
        alert('please fill all the values')
    } else if (id.length != 4) {
        alert('id length should be 4')
    }else if (isNaN(Number(price))){
        alert('price should be a number')
    }
    else {
        console.log('else')
        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:8000/myapp/add?id=${id}&name=${name}&price=${price}`,
            cache: false,
            success: (res) => {
                res = JSON.parse(res)
                if (res.result == 'success') {
                    $("#item_table_body").empty()
                    item_array = (res.array)
                    console.log(item_array)
                    item_array_required = item_array.slice(1)
                    item_array_required.forEach(element => {
                        $("#item_table_body").append(createTableRow(element.name, element.price, element.id))
                    });
                    alert('successfully added')
                }else if (res.result == 'id already exists'){
                    alert('id already exists')
                }else{
                    alert('error occured')
                }


            },
            err: (err) => {
                console.log(err)
            }
        })
    }


}
// $("button").click(function() {
//     var fired_button = $(this).val();
//     console.log(fired_button);
// });
