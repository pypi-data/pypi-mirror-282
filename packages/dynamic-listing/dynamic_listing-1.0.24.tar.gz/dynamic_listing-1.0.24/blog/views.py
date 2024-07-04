from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView

from blog.filters import BlogsFilter
from blog.models import Blog
from dynamic_listing.listing_factories import DynamicTableFactory, DynamicListFactory, DynamicGridFactory
from dynamic_listing.views import DynamicTableView, DynamicListView, DynamicGridView, BulkActionMixin


class BlogTableView(DynamicTableView):
    model = Blog
    title = "Blogs Dynamic Table View"
    filterset_class = BlogsFilter
    row_template_name = 'blog/_table_row.html'
    load_rows_from_template = True
    bulk_actions = '_bulk_actions.html',
    header_template_name = 'blog/_header.html'
    listing_actions = 'blog/_actions.html'
    modals_template_name = 'blog/_modals.html'
    table_columns = (
        ('id', "ID"),
        ('title', "Title", "text-start max-w-200px"),
        ('content', "Content", "text-center max-w-200px"),
        ('category', "Category", "text-center"),
        ('tags', "Tags", "text-center"),
        ('created_at', "Created At", "text-end"),
    )

    class Media:
        js = ('blog/blog.js',)

    def get_breadcrumb(self):
        return [
            {"title": "Home", "url": '/'},
            {"title": "Blogs"},
            {"title": "Table"}
        ]


class BlogListView(DynamicListView):
    model = Blog
    title = "Blogs Dynamic List View"
    filterset_class = BlogsFilter
    item_template_name = 'blog/_list_item.html'
    bulk_actions = '_bulk_actions.html',
    header_template_name = 'blog/_header.html'
    listing_actions = 'blog/_actions.html'
    modals_template_name = 'blog/_modals.html'

    def get_breadcrumb(self):
        return [
            {"title": "Home", "url": '/'},
            {"title": "Blogs"},
            {"title": "List"}
        ]


class BlogGridView(DynamicGridView):
    model = Blog
    title = "Blogs Dynamic Grid View"
    filterset_class = BlogsFilter
    item_template_name = 'blog/_grid_item.html'
    bulk_actions = '_bulk_actions.html',
    header_template_name = 'blog/_header.html'
    container_class = "app-container container-fluid"
    modals_template_name = 'blog/_modals.html'
    listing_actions = 'blog/_actions.html'

    def get_breadcrumb(self):
        return [
            {"title": "Home", "url": '/'},
            {"title": "Blogs"},
            {"title": "Grid"}
        ]


BlogTableFactory = DynamicTableFactory(
    model=Blog,
    load_rows_from_template=True,
    filterset_class=BlogsFilter,
    bulk_actions='_bulk_actions.html',
    row_template_name='blog/_table_row.html',
    listing_actions='blog/_actions.html',
    header_template_name='blog/_header.html',
    modals_template_name='blog/_modals.html',
    table_columns=(
        ('id', "ID"),
        ('title', "Title", "text-start max-w-200px"),
        ('content', "Content", "text-center max-w-200px"),
        ('category', "Category", "text-center"),
        ('tags', "Tags", "text-center"),
        ('created_at', "Created At", "text-end"),
    ),
    media={
        "js": ("blog/blog.js",),
    }
)

BlogListFactory = DynamicListFactory(
    model=Blog,
    filterset_class=BlogsFilter,
    listing_actions='blog/_actions.html',
    bulk_actions='_bulk_actions.html',
    item_template_name='blog/_list_item.html',
    modals_template_name='blog/_modals.html',
    header_template_name='blog/_header.html',
)

BlogGridFactory = DynamicGridFactory(
    model=Blog,
    filterset_class=BlogsFilter,
    bulk_actions='_bulk_actions.html',
    item_template_name='blog/_grid_item.html',
    listing_actions='blog/_actions.html',
    header_template_name='blog/_header.html',
    modals_template_name='blog/_modals.html'
)


class UsersTableView(DynamicTableView):
    model = User
    title = "Users"
    row_template_name = 'users/table/_table_row.html'
    load_rows_from_template = True
    table_columns = (
        ('id', "ID"),
        ('full_name', "Fullname", "text-start"),
        ('email', "Email", "text-center"),
        ('is_active', "Active", "text-center"),
        ('date_joined', "Date Joined", "text-center"),
    )


class UserDetailView(DetailView):
    model = User
    template_name = 'users/details/index.html'

    def get_listing_factory(self):
        listing_type = self.kwargs.get('listing_type', 'table')
        queryset = self.object.blog_set.all()
        factory_class = BlogTableFactory
        if listing_type == 'list':
            factory_class = BlogListFactory
        elif listing_type == 'grid':
            factory_class = BlogGridFactory

        factory = factory_class(self.request, queryset)
        factory.extra_context['blogs_count'] = queryset.count()
        factory.extra_context['csrf_token'] = self.request.COOKIES['csrftoken']
        return factory

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.get_full_name
        queryset = self.object.blog_set.all()
        context['blogs'] = self.get_listing_factory()
        return context


class BlogDeleteView(BulkActionMixin, View):
    def post(self, request, *args, **kwargs):
        input_type, value = self.get_actions_type_and_value(request.POST)
        return JsonResponse({
            "message": "Blog deleted successfully"
        })
