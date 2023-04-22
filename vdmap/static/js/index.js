$(window).on("load", () => {
    $(".switch > div").click((e) => {
        if ($(e.currentTarget).attr("activated") == '') return;
        let cur = $(".switch > div[activated]").data("target")
        $(".switch > div").attr("activated", null);
        $(e.currentTarget).attr("activated", '');
        let n = $(".switch > div[activated]").data("target")
        if (cur < n) {
            $(`.switchable[data-id=${n}]`).attr("moved-right", null)
            $(`.switchable[data-id=${cur}]`).attr("moved-left", '')
        }
        else {
            $(`.switchable[data-id=${n}]`).attr("moved-left", null)
            $(`.switchable[data-id=${cur}]`).attr("moved-right", '')
        }
    });
    $("#register-form").submit((e) => {
        e.preventDefault();
        $.post({
            url: "/auth/register",
            data: $("#register-form").serialize()
        }).done((r) => {
            console.log(r);
        });
    });
    $("#login-form").submit((e) => {
        e.preventDefault();
        $.post({
            url: "/auth/login",
            data: $("#login-form").serialize()
        }).done((r) => {
            if (r.ok) {
                window.location.href = r.redirect;
            };
        });
    });
});