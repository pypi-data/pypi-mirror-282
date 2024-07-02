from odoo import models, fields, api


class DocumentPage(models.Model):
    _inherit = "document.page"

    name = fields.Char(
        "Title",
        required=True,
        translate=True  # IMP
        )
    content = fields.Text(
        "Content",
        compute="_compute_content",
        inverse="_inverse_content",
        search="_search_content",
        required=True,
        copy=True,
        translate=True  # IMP
    )
    translated_api_content = fields.Text(
        "Content",
        compute="_compute_translated_api_content",
        store=False,
    )

    @api.multi
    def _compute_translated_api_content(self):
        for record in self:
            translated_content_record = False
            if record.content:
                translation_domain = [
                    ('name', '=', 'document.page,content'),
                    ('res_id', '=', record.id),
                    ('lang', '=', record.env.context.get('lang', self.env.user.lang)),
                    ('source', '=', record.content),
                    ('state', '=', 'translated'),
                ]
                translated_content_record = self.env['ir.translation'].search(translation_domain, limit=1)
            record.translated_api_content = translated_content_record.value if translated_content_record else record.content  # noqa

    @api.model
    def search_translated_api_content(self, search_term):
        translated_content_record = []
        if search_term:
            translation_domain = [
                ('name', '=', 'document.page,content'),
                ('lang', '=', self.env.context.get('lang', self.env.user.lang)),
                ('state', '=', 'translated'),
                ('value', 'ilike', search_term),  # no need for % since ORM already does that
            ]
            translated_content_record = self.env['ir.translation'].read_group(
                translation_domain,
                fields=["name"],
                groupby=["res_id"]
            )
        return self.browse([res.get("res_id") for res in translated_content_record])
