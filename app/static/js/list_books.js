(function () {

    const btnBuyBook = document.querySelectorAll('.btn-buy-book');
    let isbnSelectedBook = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnBuyBook.forEach((btn) => {
        btn.addEventListener('click', function(){
            isbnSelectedBook=this.id;
            confirmPurchase();
        });
    });

    const confirmPurchase = () => {
        Swal.fire({
            title: 'Confirm you want to purchase this book',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Buy',
            showLoaderOnConfirm: true,
            preConfirm: async () => {
                return await fetch(`${window.origin}/buybook`, {
                    method: 'POST',
                    mode: 'same-origin',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrf_token
                    },
                    body: JSON.stringify({
                        'isbn': isbnSelectedBook
                    })
                }).then(response => {
                    if (!response.ok) {
                        notificationSwal('Error', response.statusText, 'error', 'Close');
                    }
                    return response.json();
                }).then(data => {
                    if (data.success) {
                        notificationSwal('Great!', 'This book is yours now', 'success', 'Ok');
                    } else {
                        notificationSwal('Oops!', data.menssage, 'warning', 'Ok');
                    }
                }).catch(error => {
                    notificationSwal('Error', error, 'error', 'Close');
                });
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });
    };

})();

/*
//Código anterior
(function(){
    const btnBuyBook = document.querySelectorAll('.btn-buy-book');
    let isbnSelectedBook = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnBuyBook.forEach((btn) => {
        btn.addEventListener('click', function(){
            isbnSelectedBook=this.id;
            confirmPurchase();
        });
    });

    //Uso de Fetch API
    const confirmPurchase = async() => {

        await fetch('http://127.0.0.1:5005/buybook', {
        method:'POST',
        mode:'same-origin',
        credentials:'same-origin',
        headers:{
            'Content-Type':'application/json',
            'X-CSRF-TOKEN': csrf_token
        },
        body:JSON.stringify({
            isbn:isbnSelectedBook
        })
        }).then(response => {
            if(!response.ok){
                console.error('Error!');
            }
            return response.json();
        }).then(data => {
            console.log('Book Purchased');
        }).catch(error => {
            console.error(`error: ${error}`);
        });
    };
})();
*/