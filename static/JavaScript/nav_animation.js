counterd = 1;
$(document).ready(function () {
    $(".toggle").click(function () {
        // console.log("hello");
        $(".toggle").toggleClass("active");
        $(".sidebar").toggleClass("active");
        if (counterd % 2 == 0) {
            setTimeout(wow, 250);
            counterd++;
        } else {
            wow();
            counterd++;
        }
    });
});
function wow() {
    $(".switchToggle").toggleClass("no_dis");
    $(".profile-toggle").toggleClass("no_dis");
    $(".dnt-chkbox").toggleClass("no-dis");
    $(".all-cnt-div").toggleClass("no-dis-all-cnt-div");
}
