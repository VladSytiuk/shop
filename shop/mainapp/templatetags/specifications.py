from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>

            """

TABLE_TAIL = """
                </tbody>
                </table>
            """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Display diagonal': 'diagonal',
        'Display type': 'display_type',
        'Processor frequency': 'processor_freq',
        'RAM': 'ram',
        'Video card': 'video',
        'Time-running without charging': 'time_without_charge'
    },
    'smartphone': {
        'Screen diagonal': 'diagonal',
        'Display type': 'display_type',
        'Resolution': 'resolution',
        'Battery volume': 'battery_volume',
        'RAM': 'ram',
        'Sd': 'sd',
        'Maximum memory capacity': 'sd_memory_max',
        'Main camera': 'main_cam_mp',
        'Front camera': 'front_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

