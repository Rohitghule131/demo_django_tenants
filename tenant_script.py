from tenant_model.models import ClientModel, DomainModel

# create your public tenant
tenant = ClientModel(schema_name='public',
                     name='Schemas Inc.',
                     paid_until='2016-12-05',
                     on_trial=False)
tenant.save()

# Add one or more domains for the tenant
domain = DomainModel()
domain.domain = 'localhost'  # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()
