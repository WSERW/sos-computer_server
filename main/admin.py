from django.contrib import admin
from django.template.loader import get_template
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Course, Theme, Paragraph, CourseLevel, Spec, LevelSpec

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

class CourseAdmin(NestedModelAdmin):
    inlines = SpecInline, CourseLevelInline, ThemeInline,
    # fields = '__all__'


admin.site.register(Course, CourseAdmin)
