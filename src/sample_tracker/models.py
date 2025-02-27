from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(TimeStampedModel, models.Model):
    """Address details"""

    street = models.CharField(max_length=255, verbose_name=_("Street"), blank=True)
    ward = models.CharField(max_length=255, verbose_name=_("Ward"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    region = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Region")
    )
    postal_code = models.CharField(max_length=255, verbose_name=_("Postal Code"))

    def __str__(self):
        return f"{self.ward}, {self.district}, {self.region}"

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")


class Study(TimeStampedModel, models.Model):
    """Study details."""

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(
        max_length=50, unique=True, verbose_name=_("Study Code"), blank=True
    )
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Study")
        verbose_name_plural = _("Studies")


class StudySite(TimeStampedModel, models.Model):
    """Study site details."""

    study = models.ForeignKey(
        Study, on_delete=models.CASCADE, related_name="study_sites"
    )
    name = models.CharField(max_length=255, unique=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="study_site_address"
    )
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Study Site")
        verbose_name_plural = _("Study Sites")

    def __str__(self):
        return self.name


class Sample(TimeStampedModel, models.Model):
    """Sample details."""

    SAMPLE_TYPES = (
        ("DBS", _("Dried Blood Spot")),
        ("DNA", _("DNA Sample")),
    )

    STATUSES = (
        ("POS", _("Positive")),
        ("NEG", _("Negative")),
    )

    sample_id = models.CharField(
        max_length=100, unique=True, verbose_name=_("Sample ID")
    )
    sample_type = models.CharField(
        max_length=10, choices=SAMPLE_TYPES, verbose_name=_("Sample Type")
    )
    study_site = models.ForeignKey(
        StudySite, on_delete=models.CASCADE, verbose_name=_("Study Site")
    )
    collection_date = models.DateField(verbose_name=_("Collection Date"))
    status = models.CharField(max_length=3, choices=STATUSES, verbose_name=_("Status"))
    small_bag_number = models.CharField(
        max_length=50, blank=True, verbose_name=_("Small Bag Number")
    )
    large_bag_number = models.CharField(
        max_length=50, blank=True, verbose_name=_("Large Bag Number")
    )
    container_label = models.CharField(
        max_length=255, verbose_name=_("Container Label")
    )
    container_location = models.CharField(
        max_length=255, verbose_name=_("Container Location")
    )
    receiver_initials = models.CharField(
        max_length=10, verbose_name=_("Receiver’s Initials")
    )

    def __str__(self):
        return self.sample_id

    class Meta:
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")


class Plate(TimeStampedModel, models.Model):
    """Details about plates used for processing."""

    plate_number = models.CharField(
        max_length=50, unique=True, verbose_name=_("Plate Number")
    )
    plate_label = models.CharField(max_length=255, verbose_name=_("Plate Label"))
    status = models.CharField(
        max_length=10, choices=Sample.STATUSES, verbose_name=_("Status")
    )
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Volume (µl)")
    )
    freezer_number = models.CharField(max_length=50, verbose_name=_("Freezer Number"))
    shelf_number = models.CharField(max_length=50, verbose_name=_("Shelf Number"))

    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = _("Plate")
        verbose_name_plural = _("Plates")


class DNAExtraction(TimeStampedModel, models.Model):
    """Details about DNA extraction."""

    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE, verbose_name=_("Sample")
    )
    extraction_date = models.DateField(verbose_name=_("Extraction Date"))
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, verbose_name=_("Plate"))
    expert_initials = models.CharField(
        max_length=10, verbose_name=_("Expert’s Initials")
    )

    def __str__(self):
        return f"Extraction of {self.sample.sample_id} on {self.extraction_date}"

    class Meta:
        verbose_name = _("DNA Extraction")
        verbose_name_plural = _("DNA Extractions")


class MolecularDiagnostic(TimeStampedModel, models.Model):
    """Molecular diagnostics/genetic analysis details."""

    MOLECULAR_TECHNIQUES = (
        ("qPCR", _("qPCR")),
        ("Genotyping", _("Genotyping")),
        ("MIP", _("MIP Capture & Sequencing")),
    )

    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE, verbose_name=_("Sample")
    )
    technique = models.CharField(
        max_length=50, choices=MOLECULAR_TECHNIQUES, verbose_name=_("Technique")
    )
    processing_date = models.DateField(verbose_name=_("Processing Date"))
    plasmodium_species = models.CharField(
        max_length=50, blank=True, verbose_name=_("Plasmodium Species")
    )
    expert_initials = models.CharField(
        max_length=10, verbose_name=_("Expert’s Initials")
    )

    def __str__(self):
        return f"{self.technique} for {self.sample.sample_id}"

    class Meta:
        verbose_name = _("Molecular Diagnostic")
        verbose_name_plural = _("Molecular Diagnostics")


class Storage(TimeStampedModel, models.Model):
    """Storage details for samples and plates."""

    STORAGE_TYPES = (
        ("Archived", _("Archived")),
        ("Processing", _("Processing")),
    )

    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE, verbose_name=_("Sample")
    )
    container_number = models.CharField(
        max_length=50, verbose_name=_("Container Number")
    )
    container_label = models.CharField(
        max_length=255, verbose_name=_("Container Label")
    )
    container_location = models.CharField(
        max_length=255, verbose_name=_("Container Location")
    )
    storage_type = models.CharField(
        max_length=50, choices=STORAGE_TYPES, verbose_name=_("Storage Type")
    )
    storage_date = models.DateField(verbose_name=_("Storage Date"))
    expert_initials = models.CharField(
        max_length=10, verbose_name=_("Expert’s Initials")
    )

    def __str__(self):
        return f"Storage for {self.sample.sample_id}"

    class Meta:
        verbose_name = _("Storage")
        verbose_name_plural = _("Storages")


class QualityCheck(TimeStampedModel, models.Model):
    """Quality check results."""

    QC_STATUSES = (
        ("Accepted", _("Accepted")),
        ("Rejected", _("Rejected")),
    )

    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE, verbose_name=_("Sample")
    )
    status = models.CharField(
        max_length=10, choices=QC_STATUSES, verbose_name=_("Quality Check Status")
    )
    qc_date = models.DateField(verbose_name=_("Quality Check Date"))
    expert_initials = models.CharField(
        max_length=10, verbose_name=_("Expert’s Initials")
    )

    def __str__(self):
        return f"QC {self.status} for {self.sample.sample_id}"

    class Meta:
        verbose_name = _("Quality Check")
        verbose_name_plural = _("Quality Checks")


class Pooling(TimeStampedModel, models.Model):
    """Pooling details."""

    pooling_date = models.DateField(verbose_name=_("Pooling Date"))
    pool_name = models.CharField(max_length=255, verbose_name=_("Pool Name/Label"))
    capture_plate = models.ForeignKey(
        Plate,
        on_delete=models.CASCADE,
        related_name="pooled_capture_plate",
        verbose_name=_("Capture Plate"),
    )
    number_of_plates = models.PositiveIntegerField(verbose_name=_("Number of Plates"))
    rack_compartment_number = models.CharField(
        max_length=50, verbose_name=_("Rack/Compartment Number")
    )
    fridge_freezer_number = models.CharField(
        max_length=50, verbose_name=_("Fridge/Freezer Number")
    )
    expert_initials = models.CharField(
        max_length=10, verbose_name=_("Expert’s Initials")
    )

    def __str__(self):
        return f"Pooling: {self.pool_name} on {self.pooling_date}"

    class Meta:
        verbose_name = _("Pooling")
        verbose_name_plural = _("Pooling")


class Archive(TimeStampedModel, models.Model):
    pass
