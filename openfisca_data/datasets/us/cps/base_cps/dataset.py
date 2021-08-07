from openfisca_data.utils import *
from openfisca_data.datasets.us.cps.raw_cps import RawCPS
import h5py

PERSON_COLUMNS = (
    "person_household_id",
    "person_family_id",
    "person_id",
    "person_taxunit_id",
    "person_weight",
)

TAXUNIT_COLUMNS = (
    "taxunit_id",
    "taxunit_weight",
)

FAMILY_COLUMNS = (
    "family_id",
    "family_weight",
)

HOUSEHOLD_COLUMNS = (
    "household_id",
    "household_weight",
)


@dataset
class BaseCPS:
    name = "base_cps"
    model = US

    def generate(year):
        with RawCPS.load(year) as storage:
            person = storage.person
            family = storage.family
            household = storage.household

        person["person_household_id"] = person.PH_SEQ
        person["person_family_id"] = person.PH_SEQ * 10 + person.PF_SEQ
        person["person_id"] = person.PH_SEQ * 100 + person.P_SEQ
        person["person_taxunit_id"] = person.TAX_ID

        family["family_id"] = family.FH_SEQ * 10 + family.FFPOS
        household["household_id"] = household.H_SEQ

        person["person_weight"] = person.A_FNLWGT
        taxunit = pd.DataFrame(index=person.person_taxunit_id.unique())
        taxunit["taxunit_id"] = taxunit.index
        taxunit[
            "taxunit_weight"
        ] = 1e5  # not accurate, just a placeholder until development
        family["family_weight"] = family.FSUP_WGT
        household["household_weight"] = household.HSUP_WGT

        with h5py.File(BaseCPS.file(year), mode="w") as f:
            for col in PERSON_COLUMNS:
                f[f"{col}/{year}"] = person[col].values
            for col in FAMILY_COLUMNS:
                f[f"{col}/{year}"] = family[col].values
            for col in TAXUNIT_COLUMNS:
                f[f"{col}/{year}"] = taxunit[col].values
            for col in HOUSEHOLD_COLUMNS:
                f[f"{col}/{year}"] = household[col].values
