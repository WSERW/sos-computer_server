from django.contrib import admin
from django.template.loader import get_template
from nested_admin import NestedStackedInline, NestedModelAdmin
from import_export.admin import ImportExportMixin, ExportActionMixin


from .models import Course, Theme, Paragraph, CourseLevel, Spec, LevelSpec
from .resources import CourseResource

# Register your models here.

class ParagraphInline(NestedStackedInline):
    model = Paragraph
    # fields = '__all__'
    extra = 1

class ThemeInline(NestedStackedInline):
    model = Theme
    inlines = ParagraphInline,
    # fields = '__all__'
    extra = 1

class LevelSpecInline(NestedStackedInline):
    model = LevelSpec
    # fields = '__all__'
    extra = 1

class CourseLevelInline(NestedStackedInline):
    model = CourseLevel
    inlines = LevelSpecInline,
    # fields = '__all__'
    extra = 0

class SpecInline(NestedStackedInline):
    model = Spec
    # fields = '__all__'
    extra = 1

class CourseAdmin(ImportExportMixin,NestedModelAdmin):
    inlines = SpecInline, CourseLevelInline, ThemeInline,
    list_display = ('name', 'tag', 'is_active')
    list_filter = ('tag','demo','is_active',)
    # fields = '__all__'
    resource_class = CourseResource
    # # Подключаем ресурс для импорта
    # def get_import_resource_class(self):
    #     return CourseResource

    # # Подключаем ресурс для экспорта
    # def get_export_resource_class(self):
    #     return CourseResource


admin.site.register(Course, CourseAdmin)
