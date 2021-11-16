<template>
  <q-page>
    <banner
      banner-title="Organiser - "
      banner-description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam."
    />
  </q-page>
</template>

<script>
import Banner from '../components/Banner.vue'
export default {
  name: 'OrganiserDetailsPage',
  components: { Banner },
  data () {
    return {
      organiser: {
        username: 'lauren.rodney',
        email: 'lauren@rodney.com',
        firstName: 'Lauren',
        lastName: 'Rodney',
        photo: null
      }
    }
  },
  props: {
    id: {
      type: String,
      required: true
    }
  }
}
</script>

<style></style>
