import django_filters

from .filters import OrderingFilter, NumberInFilter, RateFilter


class FilterFieldRenderer:
    """
    Base class for rendering filter fields in a Django Filters filter set.

    This class serves as the foundation for rendering various types of filter fields within a Django Filters filter set.
    Subclasses of this renderer provide specific rendering logic for different filter types.

    :ivar template_name: The name of the template to use for rendering the filter field.
    :ivar element: The HTML element type for the filter field (e.g., 'text', 'checkbox').
    :ivar single: Indicates whether the filter field is for single selection (True) or multiple selection (False).
    :ivar name: The name of the filter field.
    :ivar filter_field: The Django Filters filter field being rendered.
    :ivar filter_type: The type of filter (e.g., 'filter', 'search', 'sort').
    :ivar form_field: The form field associated with the filter field.
    :ivar value: The current value of the filter field.

    :param filter_field: The Django Filters filter field to be rendered.
    :type filter_field: django_filters.filters.Filter
    :param form_field: The form field associated with the filter field.
    :type form_field: django.forms.Field
    :param value: The current value of the filter field.
    :type value: Any
    :param filter_type: The type of filter (default is 'filter').
    :type filter_type: str
    """

    template_name = ''
    element = None
    single = True

    def __init__(self, name, filter_field, form_field, value, filter_type='filter'):
        """
        Initialize a new FilterFieldRenderer instance.

        :param filter_field: The Django Filters filter field to be rendered.
        :type filter_field: django_filters.filters.Filter
        :param form_field: The form field associated with the filter field.
        :type form_field: django.forms.Field
        :param value: The current value of the filter field.
        :type value: Any
        :param filter_type: The type of filter (default is 'filter').
        :type filter_type: str
        """
        self.field_name = name
        self.name = filter_field.field_name
        self.filter_field = filter_field
        self.filter_type = filter_type
        self.form_field = form_field
        self.value = value

    def is_hidden(self):
        """
        Check if the filter field should be hidden in the UI.

        :return: True if the filter field should be hidden; otherwise, False.
        :rtype: bool
        """
        return True

    def get_attrs(self):
        """
        Get HTML attributes for rendering the filter field.

        :return: A dictionary of HTML attributes.
        :rtype: dict
        """
        return {
            "name": self.field_name,
            "value": self.get_value(),
            "label": self.filter_field.label,
            "type": self.element,
            "placeholder": self.form_field.field.widget.attrs[
                'placeholder'] if 'placeholder' in self.form_field.field.widget.attrs else ''
        }

    def get_value(self):
        """
        Get the current value of the filter field.

        :return: The current value of the filter field.
        :rtype: Any
        """
        return self.value

    def get_template_name(self):
        """
        Get the name of the template used for rendering the filter field.

        :return: The template name.
        :rtype: str
        """
        return self.template_name

    def get(self):
        """
        Get a dictionary representing the filter field's attributes.

        :return: A dictionary containing the filter field's attributes.
        :rtype: dict
        """
        return {
            "element": self.element,
            "template_name": self.get_template_name(),
            "type": self.filter_type,
            "single": self.single,
            "attrs": self.get_attrs()
        }

    def is_applied(self):
        """
        Check if the filter field has an applied filter.

        :return: True if the filter has an applied filter; otherwise, False.
        :rtype: bool
        """
        return self.name in self.form_field.form.data and self.form_field.form.data.get(self.name)

    def get_applied_filter(self):
        """
        Get information about the applied filter for this field.

        :return: A list containing information about the applied filter.
        :rtype: list of dict
        """
        return [
            {
                "label": self.filter_field.label,
                "key": self.name,
                "value": self.form_field.form.data.get(self.name),
                "value_label": self.get_value_label(),
            }
        ]

    def get_value_label(self):
        """
        Get a label representing the current value of the filter field.

        :return: A label for the filter field's value.
        :rtype: str
        """
        return self.form_field.form.data.get(self.name)


class NumberInFilterFieldRenderer(FilterFieldRenderer):
    element = 'number'
    single = True

    def get_template_name(self):
        return ''

    def is_hidden(self):
        return False

    def get_value(self):
        return self.form_field.form.data.get(self.name) if self.name in self.form_field.form.data \
            else 0


class NumberFilterFieldRenderer(FilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/input.html'
    element = 'number'
    single = True

    def get_attrs(self):
        attrs = super().get_attrs()
        attrs['data-instant-filter'] = "true"
        return attrs

    def is_hidden(self):
        return False

    def get_value(self):
        return self.form_field.form.data.get(self.name) if self.name in self.form_field.form.data \
            else None


class BooleanFilterFieldRenderer(FilterFieldRenderer):
    element = 'checkbox'
    single = True

    def get_template_name(self):
        if "data-switch" in self.form_field.field.widget.attrs.keys() \
                and self.form_field.field.widget.attrs["data-switch"]:
            return 'dynamic_listing/filters/fields/switch.html'
        return 'dynamic_listing/filters/fields/checkbox.html'

    def is_hidden(self):
        return False

    def get_attrs(self):
        return {
            **super(BooleanFilterFieldRenderer, self).get_attrs(),
            "checked": self.name in self.form_field.form.data and self.form_field.form.data.get(self.name)
        }

    def get_value(self):
        return 0 if self.name in self.form_field.form.data and self.form_field.form.data.get(self.name) else 1


class CharFilterFieldRenderer(FilterFieldRenderer):
    element = 'text'
    single = True

    def get_template_name(self):
        return 'dynamic_listing/filters/fields/input.html' \
            if self.filter_type != 'search' \
            else 'dynamic_listing/filters/fields/search.html'

    def is_hidden(self):
        return False

    def get_value(self):
        return self.form_field.form.data.get(self.name) if self.name in self.form_field.form.data \
            else ''


class DateTimeFilterFieldRenderer(FilterFieldRenderer):
    template_name = ''


class ChoiceFilterFieldRenderer(FilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/radio_group.html'
    single = True
    element = 'radio'

    def is_hidden(self):
        return len([choice for choice in self.form_field.field.choices if choice[0]]) <= 1

    def get_attrs(self):
        return {
            **super(ChoiceFilterFieldRenderer, self).get_attrs(),
            "choices": dict(self.form_field.field.choices)
        }

    def get_value(self):
        return self.form_field.form.data.get(
            self.name) if self.name in self.form_field.form.data and self.form_field.form.data.get(self.name) else None


class ModelChoiceFilterFieldRenderer(FilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/radio_group.html'
    single = True
    element = 'radio'

    def is_hidden(self):
        return self.form_field.field.queryset.count() <= 1

    def get_attrs(self):
        return {
            **super().get_attrs(),
            "choices": {str(item.id): str(item) for item in self.form_field.field.queryset}
        }

    def get_value(self):
        return self.form_field.form.data.get(self.name, None)

    def get_applied_filter(self):
        value = self.form_field.form.data.get(self.name)
        return [
            {
                "label": self.filter_field.label,
                "key": self.name,
                "value": value,
                "value_label": str(self.form_field.field.queryset.get(id=value)),
            }
        ]


class ModelMultipleChoiceFilterFieldRenderer(ModelChoiceFilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/checkbox_group.html'
    single = False
    element = 'checkbox'

    def is_hidden(self):
        return self.form_field.field.queryset.count() <= 1

    def get_value(self):
        return self.form_field.form.data.getlist(
            self.name) if self.form_field.form.data and self.name in self.form_field.form.data else []

    def is_applied(self):
        return self.name in self.form_field.form.data and self.form_field.form.data.getlist(self.name)

    def get_applied_filter(self):
        applied_filters = []
        for value in self.form_field.form.data.getlist(self.name):
            applied_filters.append(
                {
                    "label": self.filter_field.label,
                    "key": self.name,
                    "value": value,
                    "value_label": str(self.form_field.field.queryset.get(id=value)),
                }
            )
        return applied_filters


class OrderingFilterRenderer(ChoiceFilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/select.html'
    single = True
    element = 'select'

    def is_hidden(self):
        return len(self.form_field.field.choices) <= 1

    def get_attrs(self):
        return {
            **super(ChoiceFilterFieldRenderer, self).get_attrs(),
            "choices": dict(self.form_field.field.choices)
        }

    def get_template_name(self):
        return 'dynamic_listing/filters/fields/select.html' \
            if self.filter_type != 'sort' \
            else 'dynamic_listing/filters/fields/sort.html'


class DateFromToRangeFilterRenderer(FilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/date-range.html'

    def is_hidden(self):
        return False

    def get_value(self):
        range_from = self.name + '_after'
        range_to = self.name + '_before'
        value = ''
        if self.form_field.form.data.get(range_from, None) and self.form_field.form.data.get(range_from, None):
            value = self.form_field.form.data.get(range_from, None) + ' - ' + self.form_field.form.data.get(range_to,
                                                                                                            None)
        return {
            "range_from": self.form_field.form.data.get(range_from, None),
            "range_to": self.form_field.form.data.get(range_to, None),
            'value': value
        }

    def is_applied(self):
        range_from = self.name + '_after'
        range_to = self.name + '_before'
        data = self.form_field.form.data
        return ((range_from in data and data.get(range_from) is not None) \
                or (range_to in data and data.get(range_to) is not None))

    def get_applied_filter(self):
        range_from = self.name + '_after'
        range_to = self.name + '_before'
        data = self.form_field.form.data
        return [
            {
                "label": self.filter_field.label,
                "key": f"{range_from},{range_to}",
                "value": f"{data.get(range_from, '')},{data.get(range_to, '')}",
                "value_label": self.get_value_label(),
            }
        ]

    def get_value_label(self):
        range_from = self.name + '_after'
        range_to = self.name + '_before'
        data = self.form_field.form.data
        return f"{data.get(range_from, '')} - {data.get(range_to, '')}"


class RangeFilterRenderer(FilterFieldRenderer):
    template_name = 'dynamic_listing/filters/fields/range.html'

    def is_hidden(self):
        return False

    def get_value(self):
        range_min = self.field_name + '_min'
        range_max = self.field_name + '_max'
        value = ''
        if self.form_field.form.data.get(range_min, None) and self.form_field.form.data.get(range_min, None):
            value = self.form_field.form.data.get(range_min, None) + ' - ' + self.form_field.form.data.get(range_max,
                                                                                                           None)
        return {
            "range_min": self.form_field.form.data.get(range_min, None),
            "range_max": self.form_field.form.data.get(range_max, None),
            'value': value
        }

    def is_applied(self):
        range_min = self.field_name + '_min'
        range_max = self.field_name + '_max'
        data = self.form_field.form.data

        return ((range_min in data and data.get(range_min is not None) \
                 or (range_max in data and data.get(range_max) is not None)))

    def get_applied_filter(self):
        range_min = self.field_name + '_min'
        range_max = self.field_name + '_max'
        data = self.form_field.form.data
        return [
            {
                "label": self.filter_field.label,
                "key": f"{range_min},{range_max}",
                "value": f"{data.get(range_min, '')},{data.get(range_max, '')}",
                "value_label": self.get_value_label(),
            }
        ]

    def get_value_label(self):
        range_min = self.name + '_min'
        range_max = self.name + '_max'
        data = self.form_field.form.data
        return f"{data.get(range_min, '')} - {data.get(range_max, '')}"


FIELD_RENDERER_MAP = {
    django_filters.filters.BooleanFilter: BooleanFilterFieldRenderer,
    django_filters.filters.CharFilter: CharFilterFieldRenderer,
    django_filters.filters.ChoiceFilter: ChoiceFilterFieldRenderer,
    django_filters.filters.ModelChoiceFilter: ModelChoiceFilterFieldRenderer,
    django_filters.filters.ModelMultipleChoiceFilter: ModelMultipleChoiceFilterFieldRenderer,
    django_filters.filters.DateTimeFilter: DateTimeFilterFieldRenderer,
    django_filters.filters.DateFromToRangeFilter: DateFromToRangeFilterRenderer,
    django_filters.filters.RangeFilter: RangeFilterRenderer,
    django_filters.filters.NumberFilter: NumberFilterFieldRenderer,
    OrderingFilter: OrderingFilterRenderer,
    NumberInFilter: NumberInFilterFieldRenderer,
    RateFilter: ChoiceFilterFieldRenderer
}
