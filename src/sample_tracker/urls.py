from django.urls import path

from . import views

app_name = "sample_tracker"
urlpatterns = [
    path(
        "", views.DashboardView.as_view(), name="dashboard_home"
    ),  # Default route for the dashboard
    # =====================
    # Address URLs
    # =====================
    path("addresses/", views.AddressListView.as_view(), name="address_list"),
    path("addresses/add/", views.AddressCreateView.as_view(), name="address_create"),
    path(
        "addresses/<int:pk>/edit/",
        views.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path(
        "addresses/<int:pk>/delete/",
        views.AddressDeleteView.as_view(),
        name="address_delete",
    ),
    # =====================
    # Study URLs
    # =====================
    path("studies/", views.StudyListView.as_view(), name="study_list"),
    path("studies/<int:pk>/", views.StudyDetailView.as_view(), name="study_detail"),
    path("studies/add/", views.StudyCreateView.as_view(), name="study_create"),
    path(
        "studies/<int:pk>/edit/", views.StudyUpdateView.as_view(), name="study_update"
    ),
    path(
        "studies/<int:pk>/delete/", views.StudyDeleteView.as_view(), name="study_delete"
    ),
    # =====================
    # Study Site URLs
    # =====================
    path("study-sites/", views.StudySiteListView.as_view(), name="study_site_list"),
    path(
        "study-sites/<int:pk>/",
        views.StudySiteDetailView.as_view(),
        name="study_site_detail",
    ),
    path(
        "study-sites/add/",
        views.StudySiteCreateView.as_view(),
        name="study_site_create",
    ),
    path(
        "study-sites/<int:pk>/edit/",
        views.StudySiteUpdateView.as_view(),
        name="study_site_update",
    ),
    path(
        "study-sites/<int:pk>/delete/",
        views.StudySiteDeleteView.as_view(),
        name="study_site_delete",
    ),
    # =====================
    # Sample URLs
    # =====================
    path("samples/", views.SampleListView.as_view(), name="sample_list"),
    path("samples/<int:pk>/", views.SampleDetailView.as_view(), name="sample_detail"),
    path("samples/add/", views.SampleCreateView.as_view(), name="sample_create"),
    path(
        "samples/<int:pk>/edit/", views.SampleUpdateView.as_view(), name="sample_update"
    ),
    path(
        "samples/<int:pk>/delete/",
        views.SampleDeleteView.as_view(),
        name="sample_delete",
    ),
    # =====================
    # Plate URLs
    # =====================
    path("plates/", views.PlateListView.as_view(), name="plate_list"),
    path("plates/add/", views.PlateCreateView.as_view(), name="plate_create"),
    path("plates/<int:pk>/edit/", views.PlateUpdateView.as_view(), name="plate_update"),
    path(
        "plates/<int:pk>/delete/", views.PlateDeleteView.as_view(), name="plate_delete"
    ),
    # =====================
    # DNA Extraction URLs
    # =====================
    path(
        "dna-extractions/",
        views.DNAExtractionListView.as_view(),
        name="dna_extraction_list",
    ),
    path(
        "dna-extractions/add/",
        views.DNAExtractionCreateView.as_view(),
        name="dna_extraction_create",
    ),
    path(
        "dna-extractions/<int:pk>/edit/",
        views.DNAExtractionUpdateView.as_view(),
        name="dna_extraction_update",
    ),
    path(
        "dna-extractions/<int:pk>/delete/",
        views.DNAExtractionDeleteView.as_view(),
        name="dna_extraction_delete",
    ),
    # =====================
    # Molecular Diagnostic URLs
    # =====================
    path(
        "molecular-diagnostics/",
        views.MolecularDiagnosticListView.as_view(),
        name="molecular_diagnostic_list",
    ),
    path(
        "molecular-diagnostics/add/",
        views.MolecularDiagnosticCreateView.as_view(),
        name="molecular_diagnostic_create",
    ),
    path(
        "molecular-diagnostics/<int:pk>/edit/",
        views.MolecularDiagnosticUpdateView.as_view(),
        name="molecular_diagnostic_update",
    ),
    path(
        "molecular-diagnostics/<int:pk>/delete/",
        views.MolecularDiagnosticDeleteView.as_view(),
        name="molecular_diagnostic_delete",
    ),
    # =====================
    # Storage URLs
    # =====================
    path("storages/", views.StorageListView.as_view(), name="storage_list"),
    path("storages/add/", views.StorageCreateView.as_view(), name="storage_create"),
    path(
        "storages/<int:pk>/edit/",
        views.StorageUpdateView.as_view(),
        name="storage_update",
    ),
    path(
        "storages/<int:pk>/delete/",
        views.StorageDeleteView.as_view(),
        name="storage_delete",
    ),
    # =====================
    # Quality Check URLs
    # =====================
    path(
        "quality-checks/",
        views.QualityCheckListView.as_view(),
        name="quality_check_list",
    ),
    path(
        "quality-checks/add/",
        views.QualityCheckCreateView.as_view(),
        name="quality_check_create",
    ),
    path(
        "quality-checks/<int:pk>/edit/",
        views.QualityCheckUpdateView.as_view(),
        name="quality_check_update",
    ),
    path(
        "quality-checks/<int:pk>/delete/",
        views.QualityCheckDeleteView.as_view(),
        name="quality_check_delete",
    ),
    # =====================
    # Pooling URLs
    # =====================
    path("poolings/", views.PoolingListView.as_view(), name="pooling_list"),
    path("poolings/add/", views.PoolingCreateView.as_view(), name="pooling_create"),
    path(
        "poolings/<int:pk>/edit/",
        views.PoolingUpdateView.as_view(),
        name="pooling_update",
    ),
    path(
        "poolings/<int:pk>/delete/",
        views.PoolingDeleteView.as_view(),
        name="pooling_delete",
    ),
]
