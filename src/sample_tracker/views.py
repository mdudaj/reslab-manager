from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    AddressForm,
    DNAExtractionForm,
    MolecularDiagnosticForm,
    PlateForm,
    PoolingForm,
    QualityCheckForm,
    SampleForm,
    StorageForm,
    StudyForm,
    StudySiteForm,
)
from .models import (
    Address,
    DNAExtraction,
    MolecularDiagnostic,
    Plate,
    Pooling,
    QualityCheck,
    Sample,
    Storage,
    Study,
    StudySite,
)


class DashboardView(TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add dynamic data for the dashboard
        context["study_count"] = Study.objects.count()
        context["sample_count"] = Sample.objects.count()
        context["positive_sample_count"] = Sample.objects.filter(status="POS").count()
        context["negative_sample_count"] = Sample.objects.filter(status="NEG").count()

        # Quality Check Data
        context["accepted_quality_count"] = QualityCheck.objects.filter(
            status="Accepted"
        ).count()
        context["rejected_quality_count"] = QualityCheck.objects.filter(
            status="Rejected"
        ).count()

        # Recent Samples (Limit to 5 for display)
        context["recent_samples"] = Sample.objects.order_by("-collection_date")[:5]

        return context


# =====================
# Address Views
# =====================
class AddressListView(ListView):
    model = Address
    template_name = "address_list.html"
    context_object_name = "addresses"


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = "address_form.html"
    success_url = reverse_lazy("address_list")


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = "address_form.html"
    success_url = reverse_lazy("address_list")


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("address_list")


# =====================
# Study Views
# =====================
class StudyListView(ListView):
    model = Study
    template_name = "sample_tracker/study/study_list.html"
    context_object_name = "studies"


class StudyDetailView(DetailView):
    model = Study
    template_name = "sample_tracker/study/study_detail.html"
    context_object_name = "study"


class StudyCreateView(CreateView):
    model = Study
    form_class = StudyForm
    template_name = "sample_tracker/study/study_form.html"
    success_url = reverse_lazy("sample_tracker:study_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class StudyUpdateView(UpdateView):
    model = Study
    form_class = StudyForm
    template_name = "sample_tracker/study/study_form.html"
    success_url = reverse_lazy("sample_tracker:study_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class StudyDeleteView(DeleteView):
    model = Study
    template_name = "sample_tracker/study/confirm_delete.html"
    success_url = reverse_lazy("sample_tracker:study_list")


# =====================
# Study Site Views
# =====================
class StudySiteListView(ListView):
    model = StudySite
    template_name = "sample_tracker/study-site/study_site_list.html"
    context_object_name = "study_sites"


class StudySiteDetailView(DetailView):
    model = StudySite
    template_name = "sample_tracker/study-site/study_site_detail.html"
    context_object_name = "study_site"


class StudySiteCreateView(CreateView):
    model = StudySite
    form_class = StudySiteForm
    template_name = "sample_tracker/study-site/study_site_form.html"
    success_url = reverse_lazy("sample_tracker:study_site_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class StudySiteUpdateView(UpdateView):
    model = StudySite
    form_class = StudySiteForm
    template_name = "sample_tracker/study-site/study_site_form.html"
    success_url = reverse_lazy("sample_tracker:study_site_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class StudySiteDeleteView(DeleteView):
    model = StudySite
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("sample_tracker:study_site_list")


# =====================
# Sample Views
# =====================
class SampleListView(ListView):
    model = Sample
    template_name = "sample_tracker/sample/sample_list.html"
    context_object_name = "samples"


class SampleDetailView(DetailView):
    model = Sample
    template_name = "ssample_tracker/ample/sample_detail.html"
    context_object_name = "sample"


class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm
    template_name = "sample_tracker/sample/sample_form.html"
    success_url = reverse_lazy("sample_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class SampleUpdateView(UpdateView):
    model = Sample
    form_class = SampleForm
    template_name = "ssample_tracker/ample/sample_form.html"
    success_url = reverse_lazy("sample_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class SampleDeleteView(DeleteView):
    model = Sample
    template_name = "sample_tracker/sample/confirm_delete.html"
    success_url = reverse_lazy("sample_list")


# =====================
# Plate Views
# =====================
class PlateListView(ListView):
    model = Plate
    template_name = "plate/plate_list.html"
    context_object_name = "plates"


class PlateCreateView(CreateView):
    model = Plate
    form_class = PlateForm
    template_name = "plate/plate_form.html"
    success_url = reverse_lazy("plate_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class PlateUpdateView(UpdateView):
    model = Plate
    form_class = PlateForm
    template_name = "plate/plate_form.html"
    success_url = reverse_lazy("plate_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class PlateDeleteView(DeleteView):
    model = Plate
    template_name = "plate/confirm_delete.html"
    success_url = reverse_lazy("plate_list")


# =====================
# DNA Extraction Views
# =====================
class DNAExtractionListView(ListView):
    model = DNAExtraction
    template_name = "dna-extraction/dna_extraction_list.html"
    context_object_name = "dna_extractions"


class DNAExtractionDetailView(DetailView):
    model = DNAExtraction
    template_name = "dna-extraction/dna_extraction_detail.html"
    context_object_name = "dna_extraction"


class DNAExtractionCreateView(CreateView):
    model = DNAExtraction
    form_class = DNAExtractionForm
    template_name = "dna-extraction/dna_extraction_form.html"
    success_url = reverse_lazy("dna_extraction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class DNAExtractionUpdateView(UpdateView):
    model = DNAExtraction
    form_class = DNAExtractionForm
    template_name = "dna-extraction/dna_extraction_form.html"
    success_url = reverse_lazy("dna_extraction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class DNAExtractionDeleteView(DeleteView):
    model = DNAExtraction
    template_name = "dna-extraction/confirm_delete.html"
    success_url = reverse_lazy("dna_extraction_list")


# =====================
# Molecular Diagnostics Views
# =====================
class MolecularDiagnosticListView(ListView):
    model = MolecularDiagnostic
    template_name = "molecular-diagnostic/molecular_diagnostic_list.html"
    context_object_name = "molecular_diagnostics"


class MolecularDiagnosticDetailView(DetailView):
    model = MolecularDiagnostic
    template_name = "molecular-diagnostic/molecular_diagnostic_detail.html"
    context_object_name = "molecular_diagnostic"


class MolecularDiagnosticCreateView(CreateView):
    model = MolecularDiagnostic
    form_class = MolecularDiagnosticForm
    template_name = "molecular-diagnostic/molecular_diagnostic_form.html"
    success_url = reverse_lazy("molecular_diagnostic_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class MolecularDiagnosticUpdateView(UpdateView):
    model = MolecularDiagnostic
    form_class = MolecularDiagnosticForm
    template_name = "molecular-diagnostic/molecular_diagnostic_form.html"
    success_url = reverse_lazy("molecular_diagnostic_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class MolecularDiagnosticDeleteView(DeleteView):
    model = MolecularDiagnostic
    template_name = "molecular-diagnostic/confirm_delete.html"
    success_url = reverse_lazy("molecular_diagnostic_list")


# =====================
# Storage Views
# =====================
class StorageListView(ListView):
    model = Storage
    template_name = "storage/storage_list.html"
    context_object_name = "storages"


class StorageCreateView(CreateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage_form.html"
    success_url = reverse_lazy("storage_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class StorageUpdateView(UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage_form.html"
    success_url = reverse_lazy("storage_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class StorageDeleteView(DeleteView):
    model = Storage
    template_name = "storage/confirm_delete.html"
    success_url = reverse_lazy("storage_list")


# =====================
# Quality Check Views
# =====================
class QualityCheckListView(ListView):
    model = QualityCheck
    template_name = "quality-check/quality_check_list.html"
    context_object_name = "quality_checks"


class QualityCheckDetailView(DetailView):
    model = QualityCheck
    template_name = "quality-check/quality_check_detail.html"
    context_object_name = "quality_check"


class QualityCheckCreateView(CreateView):
    model = QualityCheck
    form_class = QualityCheckForm
    template_name = "quality-check/quality_check_form.html"
    success_url = reverse_lazy("quality_check_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class QualityCheckUpdateView(UpdateView):
    model = QualityCheck
    form_class = QualityCheckForm
    template_name = "quality-check/quality_check_form.html"
    success_url = reverse_lazy("quality_check_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class QualityCheckDeleteView(DeleteView):
    model = QualityCheck
    template_name = "quality-check/confirm_delete.html"
    success_url = reverse_lazy("quality_check_list")


# =====================
# Pooling Views
# =====================
class PoolingListView(ListView):
    model = Pooling
    template_name = "pooling/pooling_list.html"
    context_object_name = "poolings"


class PoolingDetailView(DetailView):
    model = Pooling
    template_name = "pooling/pooling_detail.html"
    context_object_name = "pooling"


class PoolingCreateView(CreateView):
    model = Pooling
    form_class = PoolingForm
    template_name = "pooling/pooling_form.html"
    success_url = reverse_lazy("pooling_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


class PoolingUpdateView(UpdateView):
    model = Pooling
    form_class = PoolingForm
    template_name = "pooling/pooling_form.html"
    success_url = reverse_lazy("pooling_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class PoolingDeleteView(DeleteView):
    model = Pooling
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("pooling_list")
