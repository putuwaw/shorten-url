function validate_form(){
    var customInput = document.getElementById("custom").value;
    var re = /^[a-zA-Z0-9_-]*$/;
    if (!re.test(customInput)){
        var errorText = document.getElementById("errorCustomURL");
        var customText = document.getElementById("postCustom");
        if (customText != null){
            customText.classList.add('hidden');
        }
        errorText.innerHTML = "Invalid custom URL! Only letters, numbers, underscores, and dashes are allowed!";
        errorText.classList.remove('hidden');
        return false;
    }
    return true;
}
var btnCopy = document.getElementById("btnCopy");
if (btnCopy != null){
    btnCopy.onclick = function(){
        var copyText = document.getElementById("copyUrl");
        copyText.select();
        copyText.setSelectionRange(0, 99999);
        navigator.clipboard.writeText(copyText.value);
        btnCopy.innerHTML = "Copied ";
        const iconCopied = document.createElement("i");
        iconCopied.classList.add("fas", "fa-clipboard-check");
        btnCopy.appendChild(iconCopied);
        const copyDefault = document.createElement("i");
        copyDefault.classList.add("fas", "fa-copy");
        setTimeout(function(){ 
            btnCopy.innerHTML = "Copy "; 
            btnCopy.appendChild(copyDefault);
        }, 1500);
    }
}