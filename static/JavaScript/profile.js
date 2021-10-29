let countera = 1;

$(document).ready(function () {
    $(".profile-toggle").click(function () {
        $(".profile-toggle").toggleClass("profile-active");
        $(".profile-sidebar").toggleClass("profile-active");
        if (countera % 2 === 0) {
            setTimeout(no_display, 200);
            countera++;
        } else {
            no_display();
            countera++;
        }
    });
});
function no_display() {
    $(".switchToggle").toggleClass("no_dis");
    $(".toggle").toggleClass("no_dis");
    $(".all-cnt-div").toggleClass("no-dis-all-cnt-div");
}
