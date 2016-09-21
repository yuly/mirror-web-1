---
---
        $(document).ready(() => {
            var update_apt_file = (ev) => {
                var sel = $(ev.target),
                    os_name = sel.find("option:selected").data('os'),
                    release_name = sel.find("option:selected").data('release'),
                    opt = sel.find('option:selected').data('opt'),
                    tmpl_selector = sel.data("template"),
                    target_selector = sel.data("target"),
                    apt_template = $.trim($(tmpl_selector).text()),
                    tmpl_data = $.extend({}, {
                        os_name: os_name,
                        release_name: release_name
                    }, opt),
                    apt_content = Mark.up(
                        apt_template,
                        tmpl_data
                    );
                $(target_selector).html(apt_content);
            };

            $("select.release-select").on('change', update_apt_file);
            $("select.release-select").each((i, e) => {
                $(e).trigger('change');
            });

        });