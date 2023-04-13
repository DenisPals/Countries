/** Store indicators that are negatively related to increase in array and get children of table row */
increase_bad = ["unemployment", "inflationrate"]
const data_values = document.getElementById("data_values").children

/** Call function */
calculate_values()

function calculate_values() {

    /** Iterate over table rows elements, dismissing the first (header) */
    for (let y = 1; y < data_values.length; y++) {
        /** If (y) element in table rows data contains a class name get its html collection*/
        if (data_values[y].className != 0) {
            value = document.getElementsByClassName(data_values[y].className)
            
            /** Iterate over tags in the array-like html collection */
            for (let i = 0; i < value.length; i++) {

                /** Store selected elements id and inner HTML in variable  */
                previous_value = parseFloat(value[i].id)
                latest_value = parseFloat(value[i].innerHTML)
                
                /** If selected element has a Country name(className) contained in bad list apply color classes accordingly */
                if (increase_bad.includes(value[i].className)) {

                    if (latest_value > previous_value) {
                        value[i].classList.add("down")
                    }
                    else if (latest_value == previous_value) {
                        value[i].classList.add("neutral")
                    }
                    else {
                        value[i].classList.add("up")
                    }
                }
                else {

                    if (latest_value > previous_value) {
                        value[i].classList.add("up")
                    }
                    else if (latest_value == previous_value) {
                        value[i].classList.add("neutral")
                    }
                    else {
                        value[i].classList.add("down")
                    }
                }
            }
        }
    }
}