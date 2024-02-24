    // Get the parent container
    var parentContainer = document.querySelector('#benHolder');

    // Counter to keep track of beneficiary numbers
    var beneficiaryCount = 2;

    // Function to add a new beneficiary
    function addBeneficiary() {
        // Create a new div element
        var newDiv = document.createElement('div');
        newDiv.className = 'd-flex flex-column justify-content-start me-2 mt-1';
        
        // Create a label element for the beneficiary
        var label = document.createElement('label');
        label.className = 'fw-light';
        label.textContent = 'Beneficiary # ' + beneficiaryCount;
        
        var delButton = document.createElement('button');
        delButton.className = 'btn btn-outline-danger btn-sm ms-1 mb-3';
        delButton.type = 'button';
        delButton.onclick = function() {
            deleteContainingDiv(this);
            };;
        delButton.style = 'padding: 0; margin:0;'
        
        var ico = document.createElement('i');
        ico.className = 'fa fa-trash';
        ico.ariaHidden = true;
        // Append the label to the new div
        newDiv.appendChild(label);
        delButton.appendChild(ico)

        // Create input elements
        var inputNames = ['Full Name', 'Relationship', 'DOB', 'Occupation', 'Employer'];
        for (var i = 0; i < inputNames.length; i++) {
            var input = document.createElement('input');
            input.className = 'form-control mb-1';
            if (inputNames[i] === 'DOB') {
                input.type = 'date';
                input.id = 'datepicker';
            } else {
                input.placeholder = inputNames[i];
            }
            newDiv.appendChild(input);
        }
        
        // Create SCC Member checkbox
        var checkboxDiv = document.createElement('div');
        checkboxDiv.className = 'form-check';
        var checkboxInput = document.createElement('input');
        checkboxInput.className = 'form-check-input';
        checkboxInput.type = 'checkbox';
        checkboxInput.name = 'flexRadioDefault';
        checkboxInput.id = 'flexRadioDefault' + beneficiaryCount;
        var checkboxLabel = document.createElement('label');
        checkboxLabel.className = 'form-check-label small-text';
        checkboxLabel.textContent = 'SCC Member?';
        checkboxLabel.setAttribute('for', 'flexRadioDefault' + beneficiaryCount);
        checkboxDiv.appendChild(checkboxInput);
        checkboxDiv.appendChild(checkboxLabel);
        newDiv.appendChild(checkboxDiv);
        
        // Append the new div to the parent container
        parentContainer.appendChild(newDiv);
        newDiv.appendChild(delButton);
        // Increment the beneficiary count
        beneficiaryCount++;
    }

    // Add click event listener to the button
    var addButton = document.getElementById('addBeneficiaryButton');
    addButton.addEventListener('click', function() {
        addBeneficiary();
    });

    function deleteContainingDiv(button) {
    const parentDiv = button.parentNode;
    if (parentDiv) {
        parentDiv.remove();
    }
    beneficiaryCount--;
    }
    
    // for address
    function handleCheckboxChange() {
      const copyCheckbox = document.getElementById('sameAddress');
      const inputbox1 = document.getElementById('curAddress');
      const inputbox2 = document.getElementById('perAddress');

      if (copyCheckbox.checked) {
        inputbox2.value = inputbox1.value;
        inputbox2.disabled = true;
      } else {
        inputbox2.value = '';
        inputbox2.disabled = false;
      }
    }
    
    const copyCheckbox = document.getElementById('sameAddress');
    copyCheckbox.addEventListener('change', handleCheckboxChange);

    // for education

    function handleEducationRadioChange() {
        const hsRadioBtn = document.getElementById('hsGrad');
    
        if (hsRadioBtn.checked) {
            $(document).ready(function() {
                $('#higherEducDiv .form-check-input').prop('disabled', false);
            });
        } else {
            $(document).ready(function() {
                $('#higherEducDiv .form-check-input').prop('disabled', true);
                
                $('#vocGrad').prop('checked', false);
                $('#vocDegree').prop('disabled', true);
                $('#vocDegree').val("");

                $('#colGrad').prop('checked', false);
                $('#colDegree').prop('disabled', true);
                $('#colDegree').val("");

                $('#posGrad').prop('checked', false);
                $('#posDegree').prop('disabled', true);
                $('#posDegree').val("");
            });
            
        }
    }
    
    // Wait for the DOM to load before adding the event listener
    document.addEventListener('DOMContentLoaded', function() {
        const hsRadioBtn = document.getElementById('hsGrad');
        const elemRadioBtn = document.getElementById('elemGrad');
        const noEducRadioBtn = document.getElementById('noEduc');
        hsRadioBtn.addEventListener('change', handleEducationRadioChange);
        elemRadioBtn.addEventListener('change', handleEducationRadioChange);
        noEducRadioBtn.addEventListener('change', handleEducationRadioChange);
    });

    // for Higher education
    document.addEventListener('DOMContentLoaded', function() {
        const vocGradCheckbox = document.getElementById('vocGrad');
        const vocDegreeInput = document.getElementById('vocDegree');

        const colGradCheckbox = document.getElementById('colGrad');
        const colDegreeInput = document.getElementById('colDegree');

        const posGradCheckbox = document.getElementById('posGrad');
        const posDegreeInput = document.getElementById('posDegree');

        vocGradCheckbox.addEventListener('change', function() {
            vocDegreeInput.disabled = !this.checked;
            vocDegreeInput.value = '';
        });

        colGradCheckbox.addEventListener('change', function() {
            colDegreeInput.disabled = !this.checked;
            colDegreeInput.value = textContent = '';
        });

        posGradCheckbox.addEventListener('change', function() {
            posDegreeInput.disabled = !this.checked;
            posDegreeInput.value = textContent = '';
        });

    });

        // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
        'use strict'
    
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.needs-validation')
    
        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }
    
            form.classList.add('was-validated')
            }, false)
        })
    })()

function convertToUpperCase(inputElement) {
    inputElement.value = inputElement.value.toUpperCase();
}