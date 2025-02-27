from django import forms

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


class AddressForm(forms.ModelForm):
    """Form for creating or updating address details."""

    class Meta:
        model = Address
        fields = ["street", "ward", "district", "region", "postal_code"]
        widgets = {
            "street": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter street"}
            ),
            "ward": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter ward"}
            ),
            "district": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter district"}
            ),
            "region": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter region"}
            ),
            "postal_code": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter postal code"}
            ),
        }


class StudyForm(forms.ModelForm):
    """Form for creating or updating a study."""

    class Meta:
        model = Study
        fields = ["name", "description", "start_date", "end_date"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter study name"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "ui input",
                    "placeholder": "Enter description",
                    "rows": 3,
                    "style": "resize:none;",
                }
            ),
            "start_date": forms.DateInput(attrs={"class": "ui input", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "ui input", "type": "date"}),
        }


class StudySiteForm(forms.ModelForm):
    """Form for creating or updating study site details."""

    class Meta:
        model = StudySite
        fields = ["study", "name", "address", "phone", "email"]
        widgets = {
            "study": forms.Select(attrs={"class": "ui dropdown"}),
            "name": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter site name"}
            ),
            "address": forms.Select(attrs={"class": "ui dropdown"}),
            "phone": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter phone number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "ui input", "placeholder": "Enter email"}
            ),
        }


class SampleForm(forms.ModelForm):
    """Form for creating or updating a sample."""

    class Meta:
        model = Sample
        fields = [
            "sample_id",
            "sample_type",
            "study_site",
            "collection_date",
            "status",
            "small_bag_number",
            "large_bag_number",
            "container_label",
            "container_location",
            "receiver_initials",
        ]
        widgets = {
            "sample_id": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter sample ID"}
            ),
            "sample_type": forms.Select(attrs={"class": "ui dropdown"}),
            "study_site": forms.Select(attrs={"class": "ui dropdown"}),
            "collection_date": forms.DateInput(
                attrs={"class": "ui input", "type": "date"}
            ),
            "status": forms.Select(attrs={"class": "ui dropdown"}),
            "small_bag_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter small bag number"}
            ),
            "large_bag_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter large bag number"}
            ),
            "container_label": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter container label"}
            ),
            "container_location": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter container location"}
            ),
            "receiver_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter receiver initials"}
            ),
        }


class PlateForm(forms.ModelForm):
    """Form for creating or updating a plate."""

    class Meta:
        model = Plate
        fields = [
            "plate_number",
            "plate_label",
            "status",
            "volume",
            "freezer_number",
            "shelf_number",
        ]
        widgets = {
            "plate_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter plate number"}
            ),
            "plate_label": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter plate label"}
            ),
            "status": forms.Select(attrs={"class": "ui dropdown"}),
            "volume": forms.NumberInput(
                attrs={"class": "ui input", "placeholder": "Enter volume in µl"}
            ),
            "freezer_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter freezer number"}
            ),
            "shelf_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter shelf number"}
            ),
        }


class DNAExtractionForm(forms.ModelForm):
    """Form for logging DNA extraction details."""

    class Meta:
        model = DNAExtraction
        fields = ["sample", "extraction_date", "plate", "expert_initials"]
        widgets = {
            "sample": forms.Select(attrs={"class": "ui dropdown"}),
            "extraction_date": forms.DateInput(
                attrs={"class": "ui input", "type": "date"}
            ),
            "plate": forms.Select(attrs={"class": "ui dropdown"}),
            "expert_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter expert initials"}
            ),
        }


class MolecularDiagnosticForm(forms.ModelForm):
    """Form for recording molecular diagnostics/genetic analysis details."""

    class Meta:
        model = MolecularDiagnostic
        fields = [
            "sample",
            "technique",
            "processing_date",
            "plasmodium_species",
            "expert_initials",
        ]
        widgets = {
            "sample": forms.Select(attrs={"class": "ui dropdown"}),
            "technique": forms.Select(attrs={"class": "ui dropdown"}),
            "processing_date": forms.DateInput(
                attrs={"class": "ui input", "type": "date"}
            ),
            "plasmodium_species": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter species"}
            ),
            "expert_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter expert initials"}
            ),
        }


class StorageForm(forms.ModelForm):
    """Form for managing sample and plate storage."""

    class Meta:
        model = Storage
        fields = [
            "sample",
            "container_number",
            "container_label",
            "container_location",
            "storage_type",
            "storage_date",
            "expert_initials",
        ]
        widgets = {
            "sample": forms.Select(attrs={"class": "ui dropdown"}),
            "container_number": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter container number"}
            ),
            "container_label": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter container label"}
            ),
            "container_location": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter location"}
            ),
            "storage_type": forms.Select(attrs={"class": "ui dropdown"}),
            "storage_date": forms.DateInput(
                attrs={"class": "ui input", "type": "date"}
            ),
            "expert_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter expert initials"}
            ),
        }


class QualityCheckForm(forms.ModelForm):
    """Form for quality check results."""

    class Meta:
        model = QualityCheck
        fields = ["sample", "status", "qc_date", "expert_initials"]
        widgets = {
            "sample": forms.Select(attrs={"class": "ui dropdown"}),
            "status": forms.Select(attrs={"class": "ui dropdown"}),
            "qc_date": forms.DateInput(attrs={"class": "ui input", "type": "date"}),
            "expert_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter expert initials"}
            ),
        }


class PoolingForm(forms.ModelForm):
    """Form for pooling details."""

    class Meta:
        model = Pooling
        fields = [
            "pooling_date",
            "pool_name",
            "capture_plate",
            "number_of_plates",
            "rack_compartment_number",
            "fridge_freezer_number",
            "expert_initials",
        ]
        widgets = {
            "pooling_date": forms.DateInput(
                attrs={"class": "ui input", "type": "date"}
            ),
            "pool_name": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter pool name"}
            ),
            "capture_plate": forms.Select(attrs={"class": "ui dropdown"}),
            "number_of_plates": forms.NumberInput(
                attrs={"class": "ui input", "placeholder": "Enter number of plates"}
            ),
            "rack_compartment_number": forms.TextInput(
                attrs={
                    "class": "ui input",
                    "placeholder": "Enter rack/compartment number",
                }
            ),
            "fridge_freezer_number": forms.TextInput(
                attrs={
                    "class": "ui input",
                    "placeholder": "Enter fridge/freezer number",
                }
            ),
            "expert_initials": forms.TextInput(
                attrs={"class": "ui input", "placeholder": "Enter expert initials"}
            ),
        }
