const getTitleMessageFromCategory = category =>{
    const titles = {
        'success': 'Bien hecho',
        'warning': 'Atención',
        'info': 'Atención',
        'error': 'Oops...',
    }
    return titles[category]
}
function showMessageAlert(category, message){
    Swal.fire({
        title: getTitleMessageFromCategory(category),
        text: message,
        icon: category
      });
}