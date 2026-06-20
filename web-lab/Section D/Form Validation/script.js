function validate() {
    const name = document.getElementById("name").value;
    const address = document.getElementById("address").value;
    const email = document.getElementById("email").value;
    const gender = document.querySelector('input[name="gender"]:checked');
    const mobile = document.getElementById("mobile").value;

    if (!name || !address || !email || !gender || !mobile) {
        alert("All fields have to be filled.");
        return false;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    const mobileDigits = mobile.replace(/\D/g, "");
    if (mobileDigits.length !== 11) {
        alert("Mobile number must be exactly 11 digits.");
        return false;
    }

    return true;
}
